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

class ActionOrientadorEstagio(Action):
	def name(self):
		return 'action_orientador_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico(5):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionCargaHorariaMinEstagio(Action):
	def name(self):
		return 'action_carga-horaria_min_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico(6):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionLimiteCreditosEstagio(Action):
	def name(self):
		return 'action_limite_creditos_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico(7):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionPreencherDatasEstagio(Action):
	def name(self):
		return 'action_preencher_datas_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico(9):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionContratosEstagio(Action):
	def name(self):
		return 'action_contratos_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico(10):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionLimiteCreditosSimultaneoEstagio(Action):
	def name(self):
		return 'action_limite_creditos_simultaneo_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico(11):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionDocMatriculaEstagio(Action):
	def name(self):
		return 'action_doc_matricula_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico(12):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionRestricaoEstagio(Action):
	def name(self):
		return 'action_restricao_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico(13):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionCoordenadoresEstagio(Action):
	def name(self):
		return 'action_coordenadores_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico(14):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionDocsNaoObrigatorioEstagio(Action):
	def name(self):
		return 'action_docs_nao_obrigatorio_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico(15):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionObjetivoEstagio(Action):
	def name(self):
		return 'action_objetivo_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico(16):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionSenhaMoodleEstagio(Action):
	def name(self):
		return 'action_senha-moodle_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico(17):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionNomeDaPastaEstagio(Action):
	def name(self):
		return 'action_nome_da_pasta_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico(18):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)
