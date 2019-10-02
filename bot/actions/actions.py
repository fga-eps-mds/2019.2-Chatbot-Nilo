from rasa_core_sdk import Action
from . import procura_respostas

class ActionAtividadesEstagio(Action):
	def name(self):
		return 'action_atividades_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico_estagio(1):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionPreRequisitosEstagio(Action):
	def name(self):
		return 'action_pre-requisitos_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico_estagio(2):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionPeriodoMatriculaEstagio(Action):
	def name(self):
		return 'action_periodo_matricula_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico_estagio(3):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionMatriculaEstagio(Action):
	def name(self):
		return 'action_matricula_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico_estagio(4):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionOrientadorEstagio(Action):
	def name(self):
		return 'action_orientador_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico_estagio(5):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionCargaHorariaMinEstagio(Action):
	def name(self):
		return 'action_carga-horaria_min_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico_estagio(6):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionLimiteCreditosEstagio(Action):
	def name(self):
		return 'action_limite_creditos_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico_estagio(7):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionLinkEstagio(Action):
	def name(self):
		return 'action_link_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico_estagio(8):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionPreencherDatasEstagio(Action):
	def name(self):
		return 'action_preencher_datas_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico_estagio(9):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionContratosEstagio(Action):
	def name(self):
		return 'action_contratos_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico_estagio(10):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionLimiteCreditosSimultaneoEstagio(Action):
	def name(self):
		return 'action_limite_creditos_simultaneo_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico_estagio(11):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionDocMatriculaEstagio(Action):
	def name(self):
		return 'action_doc_matricula_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico_estagio(12):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionRestricaoEstagio(Action):
	def name(self):
		return 'action_restricao_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico_estagio(13):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionCoordenadoresEstagio(Action):
	def name(self):
		return 'action_coordenadores_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico_estagio(14):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionDocsNaoObrigatorioEstagio(Action):
	def name(self):
		return 'action_docs_nao_obrigatorio_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico_estagio(15):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionObjetivoEstagio(Action):
	def name(self):
		return 'action_objetivo_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico_estagio(16):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionSenhaMoodleEstagio(Action):
	def name(self):
		return 'action_senha-moodle_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico_estagio(17):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionNomeDaPastaEstagio(Action):
	def name(self):
		return 'action_nome_da_pasta_estagio'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico_estagio(18):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionEncontrarGuiaCalouro(Action):
	def name(self):
		return 'action_encontrar_guia_calouro'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico_geral(1):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionQuandoEntraRiscoDesligamento(Action):
	def name(self):
		return 'action_quando_entra_risco_desligamento'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico_geral(2):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionSairRiscoDesligamento(Action):
	def name(self):
		return 'action_sair_risco_desligamento'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico_geral(3):
				dispatcher.utter_message('{}'. format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionEstudanteDesligado(Action):
	def name(self):
		return 'action_estudante_desligado'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico_geral(4):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionQuandoPedidoReIntegracao(Action):
	def name(self):
		return 'action_quando_pedido_reintegracao'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico_geral(5):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionComoPedidoReintegracao(Action):
	def name(self):
		return 'action_como_pedido_reintegracao'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico_geral(6):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)

class ActionRevisarMencao(Action):
	def name(self):
		return 'action_revisar_mencao'
	def run(self, dispatcher, tracker, domain):
		try:
			for line in procura_respostas.procura_resposta_por_topico_geral(7):
				dispatcher.utter_message('{}'.format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)