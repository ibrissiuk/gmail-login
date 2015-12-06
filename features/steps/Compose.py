import os,time,random
from selenium import webdriver
from behave import given, then, when
from support.Gmail_Page import Login
from support.Gmail_Page import Inbox
from functions.Gmail_Login import Gmail_Login
from lib.Config import Config

cf = Config()
gmail = Gmail_Login()
inbox = Inbox()
login = Login()

url = cf.get_config('config/config.ini','gmail', 'url')
logout = cf.get_config('config/config.ini','gmail', 'logout')

@given(u'I sing in to Gmail')
def impl(context):
    gmail.signin(context)
    time.sleep(3)

@when(u'I click on the Compose Button')
def step_impl(context):
    inbox.composebutton(context)
    time.sleep(2)
    assert inbox.composedialog(context)

@then(u'I sign-Out from the gmail account')
def step_impl(context):
    gmail.logout(context)