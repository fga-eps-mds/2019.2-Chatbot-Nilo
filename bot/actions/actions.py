from rasa_core_sdk import Action
from . import procura_respostas

class ActionAtividadesEstagio(Action):
	def name(self):
		return 'action_atividades_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico(1):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionPreRequisitosEstagio(Action):
	def name(self):
		return 'action_pre-requisitos_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico(2):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionPeriodoMatriculaEstagio(Action):
	def name(self):
		return 'action_periodo_matricula_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico(3):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionMatriculaEstagio(Action):
	def name(self):
		return 'action_matricula_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico(4):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)