'''The google finance page'''
import selenium

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
        return GoogleFinancePage.IsPageLoaded()


    def WaitForPageToLoad() -> bool:
        return GoogleFinancePage.GetSymbolList()


    def GetSymbolList() -> list:
        results = []
        elements:list[Webelement] = conf.Driver.Findelements(
            locator = SYMBOL_LOCATOR,
            By = By.XPATH)

        # Save the text of the elements into a list
        for element in elements:
            results.append(element.text)

        return results
