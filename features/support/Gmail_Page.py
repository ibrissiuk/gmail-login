import time
from lib.Config import Config

cf = Config()
url = cf.get_config('config/config.ini','gmail','url')
logout = cf.get_config('config/config.ini','gmail','logout')

class Login:

    def getgmail(self, context):
        context.browser.get(url)
        time.sleep(3)

    def enteremailaddress(self, context, address):
        context.browser.find_element_by_id("Email").send_keys(address)

    def nextbutton(self, context):
        context.browser.find_element_by_id('next').click()

    def enterpassword(self, context, password):
        context.browser.find_element_by_id("Passwd").send_keys(password)

    def signinbutton(self, context):
        context.browser.find_element_by_id('signIn').click()

    def logout(self, context):
        context.browser.get(logout)
        time.sleep(3)


class Inbox:

    def composebutton(self, context):
        context.browser.find_element_by_css_selector('div.T-I.J-J5-Ji.T-I-KE.L3').click()

    def composedialog(self, context):
        return context.browser.find_element_by_css_selector('div.aYF')