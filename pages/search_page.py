from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class SearchElements(object):
    SEARCH_BUTTON = (By.CLASS_NAME, 'ast-search-icon')
    SEARCH_INPUT = (By.ID, 'search-field')
    SEACH_TERMO =  (By.XPATH, '//article[1]/div/div[2]/article[1]/h3/a')

class SearchPage(BasePage):
    
    def search_button_click(self):
        wait = WebDriverWait(self.driver, 10)
        search_button = wait.until(EC.visibility_of_element_located(SearchElements.SEARCH_BUTTON))
        search_button.click()

    def search_input_sentence(self, sentence):
        wait = WebDriverWait(self.driver, 10)
        search_input = wait.until(EC.visibility_of_element_located(SearchElements.SEARCH_INPUT))
        search_input.send_keys(sentence)

    def search_input_sentence_enter(self):
        wait = WebDriverWait(self.driver, 10)
        search_input = wait.until(EC.visibility_of_element_located(SearchElements.SEARCH_INPUT))
        search_input.send_keys(Keys.ENTER)

    def search_titulo(self):
        wait = WebDriverWait(self.driver, 10)
        titulo_primeiro_link = wait.until(EC.visibility_of_element_located(SearchElements.SEACH_TERMO)).text
        return titulo_primeiro_link