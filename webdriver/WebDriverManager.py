import os
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service as EdgeService

from selenium import webdriver


class WebDriverManager:
    def __init__(self):
        self.driver = None
        self.project_root = os.path.dirname(os.path.abspath(__file__))
        self.driver_path = os.path.join(self.project_root, "..", "webdriver")

    def create_edge_driver(self):
        edge_exe = os.path.join(self.driver_path, "msedgedriver.exe")

        if not os.path.exists(edge_exe):
            raise FileNotFoundError(f"Edge WebDriver no encontrado en: {edge_exe}")

        options = Options()
        options.add_argument("--start-maximized")
        service = EdgeService(executable_path=edge_exe)

        try:
            self.driver = webdriver.Edge(service=service, options=options)
        except Exception as e:
            raise RuntimeError(f"Error al iniciar Edge WebDriver: {e}")

        return self.driver

    #   def create_chrome_driver(self):
    #       chrome_exe = os.path.join(self.driver_path, "chromedriver.exe")
    #       service = ChromeService(executable_path=chrome_exe)
    #       self.driver = webdriver.Chrome(service=service)
    #       return self.driver

    def quit_driver(self):
        if self.driver:
            self.driver.quit()