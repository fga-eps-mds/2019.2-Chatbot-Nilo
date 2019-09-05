from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import os
import json
import typing

from typing import Any, List, Text

from rasa_core import utils
from rasa_core.policies.policy import Policy
from rasa_core.constants import FALLBACK_SCORE

logger = logging.getLogger(__name__)

if typing.TYPE_CHECKING:
    from rasa_core.domain import Domain
    from rasa_core.trackers import DialogueStateTracker


class CustomFallbackPolicy(Policy):
    """Policy which executes a fallback action if NLU confidence is low
        or no other policy has a high-confidence prediction.

        :param float nlu_threshold:
          minimum threshold for NLU confidence.
          If intent prediction confidence is lower than this,
          predict fallback action with confidence 1.0.

        :param float core_threshold:
          if NLU confidence threshold is met,
          predict fallback action with confidence `core_threshold`.
          If this is the highest confidence in the ensemble,
          the fallback action will be executed.

        :param Text fallback_action_name:
          name of the action to execute as a fallback.
    """

    @staticmethod
    def _standard_featurizer():
        return None

    def __init__(self,
                 nlu_threshold=0.6,  # type: float
                 core_threshold=0.6,  # type: float
                 fallback_action_name="action_default_fallback"  # type: Text
                 ):
        # type: (...) -> None

        super(CustomFallbackPolicy, self).__init__()

        self.nlu_threshold = nlu_threshold
        self.core_threshold = core_threshold
        self.fallback_action_name = fallback_action_name

    def train(self,
              training_trackers,  # type: List[DialogueStateTracker]
              domain,  # type: Domain
              **kwargs  # type: Any
              ):
        # type: (...) -> None
        """Does nothing. This policy is deterministic."""

        pass

    def should_fallback(self,
                        nlu_confidence,  # type float
                        last_action_name  # type: Text
                        ):
        # type: (...) -> bool
        """It should predict fallback action only if
        a. predicted NLU confidence is lower than ``nlu_threshold`` &&
        b. last action is NOT fallback action
        """
        trigger = False
        if nlu_confidence < self.nlu_threshold:
            trigger = True
        if last_action_name == self.fallback_action_name:
            trigger = False
        if last_action_name is None:
            trigger = False
            logger.debug("Last action_name is None")

        return trigger

    def fallback_scores(self, domain, fallback_score=FALLBACK_SCORE):
        """Prediction scores used if a fallback is necessary."""
        result = [0.0] * domain.num_actions
        idx = domain.index_for_action(self.fallback_action_name)
        result[idx] = fallback_score
        return result

    def predict_action_probabilities(self, tracker, domain):
        # type: (DialogueStateTracker, Domain) -> List[float]
        """Predicts a fallback action if NLU confidence is low
            or no other policy has a high-confidence prediction"""

        nlu_data = tracker.latest_message.parse_data
        # logger.debug("this is the last message {}".format(nlu_data))
        # if NLU interpreter does not provide confidence score,
        # it is set to 1.0 here in order
        # to not override standard behaviour
        nlu_confidence = nlu_data["intent"].get("confidence", 1.0)
        # logger.debug("NLU_DATA [intent] = {}".format(nlu_data["intent"]))
        # core_confidence = tracker.current_state()
        # logger.debug("This should be core_confidence {}"
        # .format(core_confidence))

        # if tracker.latest_action_name == self.fallback_action_name:
        #     result = [0.0] * domain.num_actions
        #     idx = domain.index_for_action('action_listen')
        #     result[idx] = FALLBACK_SCORE
        #     logger.debug("FALLBACK_SCORE = {}".format(FALLBACK_SCORE))

        if self.should_fallback(nlu_confidence, tracker.latest_action_name):
            logger.debug("NLU confidence {} is lower "
                         "than NLU threshold {}. "
                         "Predicting fallback action: {}"
                         "".format(nlu_confidence, self.nlu_threshold,
                                   self.fallback_action_name))
            # we set this to 1.1 to make sure fallback overrides
            # the memoization policy
            result = self.fallback_scores(domain)
        else:
            # NLU confidence threshold is met, so
            # predict fallback action with confidence `core_threshold`
            # if this is the highest confidence in the ensemble,
            # the fallback action will be executed.
            result = self.fallback_scores(domain, self.core_threshold)
            try:
                if (tracker.latest_action_name !=
                        nlu_data["intent"].get('name')):
                    if (nlu_data["intent"].get('confidence') >
                            self.core_threshold):
                        idx = domain.index_for_action("utter_{}".format(
                                                      nlu_data["intent"]
                                                      .get('name')))
                        result[idx] = (nlu_data["intent"]
                                       .get('confidence',
                                       self.nlu_threshold))
            except Exception:
                pass
            # logger.debug("else result= {}".format(result))
            # result = [0.0] * domain.num_actions
            # result[idx] = FALLBACK_SCORE
            # logger.debug("FALLBACK_SCORE = {}".format(FALLBACK_SCORE))
        return result

    def persist(self, path):
        # type: (Text) -> None
        """Persists the policy to storage."""
        config_file = os.path.join(path, 'custom_fallback_policy.json')
        meta = {
            "nlu_threshold": self.nlu_threshold,
            "core_threshold": self.core_threshold,
            "fallback_action_name": self.fallback_action_name
        }
        utils.create_dir_for_file(config_file)
        utils.dump_obj_as_json_to_file(config_file, meta)

    @classmethod
    def load(cls, path):
        meta = {}
        if os.path.exists(path):
            meta_path = os.path.join(path, "custom_fallback_policy.json")
            if os.path.isfile(meta_path):
                meta = json.loads(utils.read_file(meta_path))

        return cls(**meta)
