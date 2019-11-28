from rasa_core_sdk import Action
import telegram
from . import webscraping


class ActionEnviarDocFaqEstagio(Action):
    def name(self):
        return "action_enviar_doc_faq_estagio"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Eu tenho muitas informações sobre estágio " +
                                 "para você, Vossa Majestade!")
        dispatcher.utter_message("Estou te enviando um documento com as " +
                                 "dúvidas mais pertinentes que os alunos " +
                                 "costumam ter")
        try:
            bot = telegram.Bot(token='TELEGRAM_TOKEN')
            url = 'https://www.docdroid.net/file/download/RdSYmiN'
            url += '/faq-estagio-supervisionado.pdf'
            bot.sendDocument(chat_id=tracker.sender_id, document=url)
        except:
            dispatcher.utter_message("Não consegui acessar o documento :/")
            dispatcher.utter_message("Mas você pode me perguntar sua dúvida" +
                                     " específica que eu farei o máximo para" +
                                     " te responder!")


class ActionEnviarTCEPA(Action):
    def name(self):
        return "action_enviar_tce_pa"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Eu tenho esses documentos de estágio" +
                                 " supervisionado e não-obrigatório!")
        dispatcher.utter_message("Estou te enviando o TCE e o PA")
        try:
            bot = telegram.Bot(token='TELEGRAM_TOKEN')
            url = 'https://fga.unb.br/articles/0002/2354'
            url += '/tce_para_estagio_obrigatorio.pdf'
            bot.sendDocument(chat_id=tracker.sender_id, document=url)
            url2 = 'https://fga.unb.br/articles/0002/2356/'
            url2 += 'tce_para_estagio_nao_obrigatorio.pdf'
            bot.sendDocument(chat_id=tracker.sender_id, document=url2)
        except:
            dispatcher.utter_message("Infelizmente não consegui acessar o" +
                                     " documento que Vossa Majestade" +
                                     " pediu :/")


class ActionEnviarFichaSolicitacao(Action):
    def name(self):
        return "action_enviar_ficha_solicitacao"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Eu tenho a ficha de solicitação " +
                                 "de matrícula em estágio supervisionado!")
        dispatcher.utter_message("Se você já estiver cadastrado na matéria," +
                                 " pode acessar uma ficha de preenchimento " +
                                 "automático pelo moodle.")
        dispatcher.utter_message("Estou te enviando a Ficha de Solicitação " +
                                 "de Matrícula.")
        try:
            bot = telegram.Bot(token='TELEGRAM_TOKEN')
            url = 'https://aprender.ead.unb.br/pluginfile.php/610764'
            url += '/mod_resource/content/2/Anexo1_Ficha_'
            url += 'Matr%C3%ADcula_Est%C3%A1gio_Supervisionado_FGA.pdf'
            bot.sendDocument(chat_id=tracker.sender_id, document=url)
        except:
            dispatcher.utter_message("Infelizmente não consegui acessar o" +
                                     " documento que Vossa Majestade" +
                                     " pediu :/")


class ActionEnviarModeloDeTermoAditivo(Action):
    def name(self):
        return "action_enviar_modelo_de_termo_aditivo"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Eu tenho o modelo de termo " +
                                 "aditivo para te enviar!")
        dispatcher.utter_message("Estou te enviando agora.")
        try:
            bot = telegram.Bot(token='TELEGRAM_TOKEN')
            url = 'https://fga.unb.br/articles/0002/2352'
            url += '/termo_aditivo_ao_tce.pdf'
            bot.sendDocument(chat_id=tracker.sender_id, document=url)
        except:
            dispatcher.utter_message("Infelizmente não consegui acessar o" +
                                     " documento que Vossa Majestade" +
                                     " pediu :/")


class ActionEnviarModeloDeTermoRescisorio(Action):
    def name(self):
        return "action_enviar_termo_rescisorio"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Eu tenho o modelo de termo " +
                                 "rescisório para te enviar!")
        dispatcher.utter_message("Estou te enviando agora.")
        try:
            bot = telegram.Bot(token='TELEGRAM_TOKEN')
            url = 'https://fga.unb.br/articles/0002/2351'
            url += '/termo_de_rescisorio.pdf'
            bot.sendDocument(chat_id=tracker.sender_id, document=url)
        except:
            dispatcher.utter_message("Infelizmente não consegui acessar o" +
                                     " documento que Vossa Majestade" +
                                     " pediu :/")


class ActionTodosOsCoordenadores(Action):
    def name(self):
        return "action_todos_os_coordenadores"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Então Vossa Majestade quer " +
                                 "encontrar os Deuses...")
        dispatcher.utter_message("Só um instante... Estou tentando " +
                                 "lembrar o nome de todos...")
        try:
            web = webscraping.WebScrapingIntegration()
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
        except:
            dispatcher.utter_message("Infelizmente não consegui acessar o" +
                                     " site com as informações sobre os " +
                                     " coordenadores.")
            dispatcher.utter_message("Mas você pode obter essa informação " +
                                     "entrando em contato com a coordenação" +
                                     " da FGA.")


class ActionCoordenadorDeSoftware(Action):
    def name(self):
        return "action_coordenador_de_software"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Então Vossa Majestade finalmente se " +
                                 "tornará um(a) grande desenvolvedor(a)")
        dispatcher.utter_message("Só um instante... Estou buscando o " +
                                 "guia certo para lhe ajudar")
        try:
            web = webscraping.WebScrapingIntegration()
            dispatcher.utter_message(web.software_coordinator())
        except:
            dispatcher.utter_message("Infelizmente não consegui acessar o" +
                                     " site com as informações sobre os " +
                                     " coordenadores.")
            dispatcher.utter_message("Mas você pode obter essa informação " +
                                     "entrando em contato com a coordenação" +
                                     " da FGA.")


class ActionCoordenadorDeEnergia(Action):
    def name(self):
        return "action_coordenador_de_energia"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Tomara que você faça um sistema para " +
                                 "captar toda a energia solar do deserto" +
                                 "do Egito!")
        dispatcher.utter_message("Só um instante... Estou buscando o guia" +
                                 "certo para lhe ajudar")
        try:
            web = webscraping.WebScrapingIntegration()
            dispatcher.utter_message(web.energy_coordinator())
        except:
            dispatcher.utter_message("Infelizmente não consegui acessar o" +
                                     " site com as informações sobre os " +
                                     " coordenadores.")
            dispatcher.utter_message("Mas você pode obter essa informação " +
                                     "entrando em contato com a coordenação" +
                                     " da FGA.")


class ActionCoordenadorDeAeroespacial(Action):
    def name(self):
        return "action_coordenador_de_aeroespacial"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Tomara que Vossa Majestade construa um" +
                                 "avião para que possa visitar o Egito...")
        dispatcher.utter_message("Só um instante... Estou buscando o guia" +
                                 "certo para lhe ajudar")
        try:
            web = webscraping.WebScrapingIntegration()
            dispatcher.utter_message(web.aeroespace_coordinator())
        except:
            dispatcher.utter_message("Infelizmente não consegui acessar o" +
                                     " site com as informações sobre os " +
                                     " coordenadores.")
            dispatcher.utter_message("Mas você pode obter essa informação " +
                                     "entrando em contato com a coordenação" +
                                     " da FGA.")


class ActionCoordenadorDeEletronica(Action):
    def name(self):
        return "action_coordenador_de_eletronica"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("UAU espero que Vossa Majestade possa " +
                                 "criar várias coisas incriveis...")
        dispatcher.utter_message("Só um instante... Estou buscando o" +
                                 "guia certo para lhe ajuda")
        try:
            web = webscraping.WebScrapingIntegration()
            dispatcher.utter_message(web.eletronics_coordinator())
        except:
            dispatcher.utter_message("Infelizmente não consegui acessar o" +
                                     " site com as informações sobre os " +
                                     " coordenadores.")
            dispatcher.utter_message("Mas você pode obter essa informação " +
                                     "entrando em contato com a coordenação" +
                                     " da FGA.")


class ActionCoordenadorDeAutomotiva(Action):
    def name(self):
        return "action_coordenador_de_automotiva"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Então Vossa Majestade finalmente está " +
                                 "pronto para construir os carros que " +
                                 "desbravarão o deserto...")
        dispatcher.utter_message("Só um instante... Estou buscando " +
                                 "o guia certo para lhe ajudar")
        try:
            web = webscraping.WebScrapingIntegration()
            dispatcher.utter_message(web.automotive_coordinator())
        except:
            dispatcher.utter_message("Infelizmente não consegui acessar o" +
                                     " site com as informações sobre os " +
                                     " coordenadores.")
            dispatcher.utter_message("Mas você pode obter essa informação " +
                                     "entrando em contato com a coordenação" +
                                     " da FGA.")
