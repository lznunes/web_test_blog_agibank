import os
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

# Configuração do driver

#def get_driver(headless=False): #Remover comentario quando executar localmente para que o browser seja executado mod grafico
def get_driver(headless=True): #Comentar linha para executar testes sem modo gráfico
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    return driver

@pytest.fixture
def driver_setup():
    driver = get_driver(headless=os.getenv('HEADLESS') == 'True')
    yield driver
    driver.quit()
