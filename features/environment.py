import os

from dotenv import load_dotenv

from webdriver.WebDriverManager import WebDriverManager
def before_all(context):
    load_dotenv(dotenv_path="enviroment.env")
    load_dotenv()
    context.password = os.getenv("LOGIN_PASSWORD")
    context.driver_manager = WebDriverManager()
    #context.driver = context.driver_manager.create_chrome_driver()
    context.driver = context.driver_manager.create_edge_driver()
    print("Edge driver creado")

def after_all(context):
    context.driver_manager.quit_driver()
    print("Edge driver cerrado")
