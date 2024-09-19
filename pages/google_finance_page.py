'''The page base'''
from time import sleep
from selenium.webdriver.common.by import By

import config.config
from pages.page_base import PageBase


# Locators
SYMBOL_LOCATOR = '//div[@id="smart-watchlist-title"]/../ul/li//div/div/div[1]/div/div/div' # XPATH

# Local Variables
conf = config.config.Config

class GoogleFinancePage(PageBase):

    def __init__(self):
        super().__init__(
            name = 'Google Finance',
            is_loaded_locator = 'smart-watchlist-title',
            by = By.ID)


    def GetSymbolList(self) -> list:
        results = []
        elements:list = conf.Driver.find_elements(
            value = SYMBOL_LOCATOR,
            by = By.XPATH)

        # Save the text of the elements into a list
        for element in elements:
            results.append(element.text)

        return results

