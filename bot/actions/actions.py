from rasa_core_sdk import Action
import telegram
from . import webscraping

class ActionEnviarDocFaqEstagio(Action):
    def name(self):
        return "action_enviar_doc_faq_estagio"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Eu tenho muitas informações sobre estágio para você, Vossa Majestade!")
        dispatcher.utter_message("Estou te enviando um documento com as dúvidas mais pertinentes que os alunos costumam ter")
        bot = telegram.Bot(token='ACCESS_TOKEN')
        url = 'https://aprender.ead.unb.br/pluginfile.php/688847/mod_resource/content/5/faq_estagio_supervisionado.pdf'
        bot.sendDocument(chat_id=tracker.sender_id,document=url)

class ActionTodosOsCoordenadores(Action):
	def name(self):
		return "action_todos_os_coordenadores"

	def run(self, dispatcher, tracker, domain):
		dispatcher.utter_message("Em alguns instantes terei a lista de coordenadores e conseguirei informar Vossa Majestade...")
		dispatcher.utter_message(webscraping.all_cordinators())
