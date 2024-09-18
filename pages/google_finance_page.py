'''The google finance page'''
from time import sleep
from selenium.webdriver.common.by import By

import config.config


# Locators
TEXT_LOCATOR = 'smart-watchlist-title' # ID
SYMBOL_LOCATOR = '//div[@id="smart-watchlist-title"]/../ul/li//div/div/div[1]/div/div/div' # XPATH

# Local Variables
conf = config.config.Config

class GoogleFinancePage():

    property
    Name = 'Google Finance'

    def IsPageLoaded() -> bool:
        return conf.Driver.find_element(
            value = TEXT_LOCATOR,
            by = By.ID).is_displayed()


    def WaitForPageToLoad(timeout:int = 30) -> bool:
        timer:int = 0
        while not GoogleFinancePage.IsPageLoaded() & timer < timeout:
            timer += 2
            sleep(2)
        return GoogleFinancePage.IsPageLoaded()       


    def GetSymbolList() -> list:
        results = []
        elements:list = conf.Driver.find_elements(
            value = SYMBOL_LOCATOR,
            by = By.XPATH)

        # Save the text of the elements into a list
        for element in elements:
            results.append(element.text)

        return results

