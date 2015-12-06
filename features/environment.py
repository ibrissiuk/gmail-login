from selenium import webdriver


def before_step(context, step):
	context.step = step
	src = context.browser.page_source

def before_scenario(context, scenario):
	context.browser = webdriver.Firefox()
	context.browser.set_window_size(2000, 2000)
	context.browser.maximize_window()

def after_scenario(context, scenario):
	context.browser.quit()