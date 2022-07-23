import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class Edge():

    def edge_config(self):
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

        driver.get('https://google.com')
        time.sleep(3)

        driver.close()


obj = Edge()
obj.edge_config()
