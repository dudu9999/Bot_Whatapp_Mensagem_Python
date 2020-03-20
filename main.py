from selenium import webdriver
import time

class whatsappbot:
    def __init__(self):
        self.mensagem = "Olá estou testando o meu bot que fiz com pythom!"
        self.grupos = ["Grupo de teste"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):
        print('fjjbifakkb')
        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chat_bot = self.driver.find_element_by_class_name('_13mgZ')
            time.sleep(3)
            chat_bot.click()
            chat_bot.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath(f"//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)

bot = whatsappbot()
bot.EnviarMensagens()
print("Fim da execução")
