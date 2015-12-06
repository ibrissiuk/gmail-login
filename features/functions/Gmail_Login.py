import time
from support.Gmail_Page import Login
from support.Gmail_Page import Inbox

lg = Login()
inbox = Inbox()
address = "jan.barsik"
password = "Test12345"

class Gmail_Login:

    def signin(self, context):
        lg.getgmail(context)
        lg.enteremailaddress(context, address)
        lg.nextbutton(context)
        time.sleep(2)
        lg.enterpassword(context, password)
        lg.signinbutton(context)
        time.sleep(2)

    def logout(self, context):
        lg.logout(context)
        time.sleep(2)
        assert lg.enterpassword