from pages.base_page import BasePage

class MainPage(BasePage):
    def open_page(self, page):
        self.driver.get(page)
