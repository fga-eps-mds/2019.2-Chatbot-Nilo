from rasa_core_sdk import Action
import telegram
from . import webscraping

class ActionEnviarDocFaqEstagio(Action):
	def name(self):
		return "action_enviar_doc_faq_estagio"

	def run(self, dispatcher, tracker, domain):
		dispatcher.utter_message("Eu tenho muitas informações sobre estágio para você, Vossa Majestade!")
		dispatcher.utter_message("Estou te enviando um documento com as dúvidas mais pertinentes que os alunos costumam ter")
		bot = telegram.Bot(token='TELEGRAM_TOKEN')
		url = 'https://aprender.ead.unb.br/pluginfile.php/688847/mod_resource/content/5/faq_estagio_supervisionado.pdf'
		bot.sendDocument(chat_id=tracker.sender_id,document=url)

class ActionEnviarTCEPA(Action):
	def name(self):
		return "action_enviar_tce_pa"

	def run(self, dispatcher, tracker, domain):
		dispatcher.utter_message("Eu tenho esses documentos de estágio supervisionado e não-obrigatório!")
		dispatcher.utter_message("Estou te enviando o TCE e o PA")
		bot = telegram.Bot(token='TELEGRAM_TOKEN')
		url = 'https://fga.unb.br/articles/0002/2354/tce_para_estagio_obrigatorio.pdf'
		bot.sendDocument(chat_id=tracker.sender_id,document=url)
		url2 = 'https://fga.unb.br/articles/0002/2356/tce_para_estagio_nao_obrigatorio.pdf'
		bot.sendDocument(chat_id=tracker.sender_id,document=url2)

class ActionEnviarFichaSolicitacao(Action):
	def name(self):
		return "action_enviar_ficha_solicitacao"

	def run(self, dispatcher, tracker, domain):
		dispatcher.utter_message("Eu tenho a ficha de solicitação de matrícula em estágio supervisionado!")
		dispatcher.utter_message("Se você já estiver cadastrado na matéria, pode acessar uma ficha de preenchimento automático pelo moodle.")
		dispatcher.utter_message("Estou te enviando a Ficha de Solicitação de Matrícula.")
		bot = telegram.Bot(token='TELEGRAM_TOKEN')
		url = 'https://aprender.ead.unb.br/pluginfile.php/610764/mod_resource/content/2/Anexo1_Ficha_Matr%C3%ADcula_Est%C3%A1gio_Supervisionado_FGA.pdf'
		bot.sendDocument(chat_id=tracker.sender_id,document=url)

class ActionEnviarModeloDeTermoAditivo(Action):
	def name(self):
		return "action_enviar_modelo_de_termo_aditivo"

	def run(self, dispatcher, tracker, domain):
		dispatcher.utter_message("Eu tenho o modelo de termo aditivo para te enviar!")
		dispatcher.utter_message("Estou te enviando agora.")
		bot = telegram.Bot(token='TELEGRAM_TOKEN')
		url = 'https://fga.unb.br/articles/0002/2352/termo_aditivo_ao_tce.pdf'
		bot.sendDocument(chat_id=tracker.sender_id, document = url)

class ActionEnviarModeloDeTermoRescisorio(Action):
	def name(self):
		return "action_enviar_termo_rescisorio"

	def run(self, dispatcher, tracker, domain):
		dispatcher.utter_message("Eu tenho o modelo de termo rescisório para te enviar!")
		dispatcher.utter_message("Estou te enviando agora.")
		bot = telegram.Bot(token='TELEGRAM_TOKEN')
		url = 'https://fga.unb.br/articles/0002/2351/termo_de_rescisorio.pdf'
		bot.sendDocument(chat_id=tracker.sender_id, document = url)

class ActionTodosOsCoordenadores(Action):
	def name(self):
		return "action_todos_os_coordenadores"

	def run(self, dispatcher, tracker, domain):
		web = webscraping.WebScrapingIntegration()
		dispatcher.utter_message("Então Vossa Majestade quer encontrar os Deuses...")
		dispatcher.utter_message("Só um instante... Estou tentando lembrar o nome de todos...")
		dispatcher.utter_message("Eng. Aeroespacial:")
		dispatcher.utter_message(web.aeroespace_coordinator())
		dispatcher.utter_message("Eng. Automotiva:")
		dispatcher.utter_message(web.automotive_coordinator())
		dispatcher.utter_message("Eng. Eletrônica:")
		dispatcher.utter_message(web.eletronics_coordinator())
		dispatcher.utter_message("Eng. de Software:")
		dispatcher.utter_message(web.software_coordinator())
		dispatcher.utter_message("Eng. de Energia:")
		dispatcher.utter_message(web.energy_coordinator())

class ActionCoordenadorDeSoftware(Action):
	def name(self):
		return "action_coordenador_de_software"

	def run(self, dispatcher, tracker, domain):
		web = webscraping.WebScrapingIntegration()
		dispatcher.utter_message("Então Vossa Majestade finalmente se tornará um(a) grande desenvolvedor(a)")
		dispatcher.utter_message("Só um instante... Estou buscando o guia certo para lhe ajudar")
		dispatcher.utter_message(web.software_coordinator())

class ActionCoordenadorDeEnergia(Action):
	def name(self):
		return "action_coordenador_de_energia"

	def run(self, dispatcher, tracker, domain):
		web = webscraping.WebScrapingIntegration()
		dispatcher.utter_message("Tomara que você faça um sistema para captar toda a energia solar do deserto do Egito!")
		dispatcher.utter_message("Só um instante... Estou buscando o guia certo para lhe ajudar")
		dispatcher.utter_message(web.energy_coordinator())

class ActionCoordenadorDeAeroespacial(Action):
	def name(self):
		return "action_coordenador_de_aeroespacial"

	def run(self, dispatcher, tracker, domain):
		web = webscraping.WebScrapingIntegration()
		dispatcher.utter_message("Tomara que Vossa Majestade construa um avião para que possa visitar o Egito...")
		dispatcher.utter_message("Só um instante... Estou buscando o guia certo para lhe ajudar")
		dispatcher.utter_message(web.aeroespace_coordinator())

class ActionCoordenadorDeEletronica(Action):
	def name(self):
		return "action_coordenador_de_eletronica"

	def run(self, dispatcher, tracker, domain):
		web = webscraping.WebScrapingIntegration()
		dispatcher.utter_message("UAU espero que Vossa Majestade possa criar várias coisas incriveis...")
		dispatcher.utter_message("Só um instante... Estou buscando o guia certo para lhe ajuda")
		dispatcher.utter_message(web.eletronics_coordinator())

class ActionCoordenadorDeAutomotiva(Action):
	def name(self):
		return "action_coordenador_de_automotiva"

	def run(self, dispatcher, tracker, domain):
		web = webscraping.WebScrapingIntegration()
		dispatcher.utter_message("Então Vossa Majestade finalmente está pronto para construir os carros que desbravarão o deserto...")
		dispatcher.utter_message("Só um instante... Estou buscando o guia certo para lhe ajudar")
		dispatcher.utter_message(web.automotive_coordinator())