'''The google finance page'''
from time import sleep
from selenium.webdriver.common.by import By

import config.config


# Local Variables
conf = config.config.Config

class PageBase():

    def __init__(self, name:str, is_loaded_locator:str, by:By):
        self.driver = conf.Driver
        self.page_name = name
        self.page_locator = is_loaded_locator
        self.by = by


    def IsPageLoaded(self) -> bool:
        return conf.Driver.find_element(
            value = self.page_locator,
            by = self.by).is_displayed()


    def WaitForPageToLoad(self,timeout:int = 30) -> bool:
        timer:int = 0
        while not self.IsPageLoaded() & timer < timeout:
            timer += 2
            sleep(2)
        return self.IsPageLoaded()       
