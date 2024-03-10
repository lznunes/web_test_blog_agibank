from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ResultElements(object):
    SEACH_RESULT = (By.CLASS_NAME, 'page-title')
    SEACH_NOT_FOUND_TEXT = (By.CLASS_NAME, 'no-results')


class ResultPage(BasePage):
        
    def search_result_title(self):
        wait = WebDriverWait(self.driver, 10)
        result_title = wait.until(EC.visibility_of_element_located(ResultElements.SEACH_RESULT)).text
        return result_title  
        
    def search_label_not_fount(self):    
        try:
            wait = WebDriverWait(self.driver, 10)
            label_not_found = wait.until(EC.visibility_of_element_located(ResultElements.SEACH_NOT_FOUND_TEXT)).text
            return label_not_found
        except TimeoutException:
            return False  
    