import threading
from wsgiref.simple_server import demo_app, make_server
from selenium import webdriver

from dojo import views


def before_all(context):
    context.server = make_server('', 8000, demo_app)
    context.server.set_app(views.app)
    context.thread = threading.Thread(target=context.server.serve_forever)
    context.thread.start()
    context.browser = webdriver.Firefox()


def after_all(context):
    context.server.shutdown()
    context.thread.join()
    context.browser.quit()
