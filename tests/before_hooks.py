'''Before test hooks'''
from selenium.webdriver import Chrome, ChromeOptions

import config.config


# Local Variables
conf = config.config.Config

class BeforeHooks():
    '''Before test hooks class'''

    def BeforeAll():
        options = ChromeOptions()
        options.add_argument('--headless')
        conf.Driver = Chrome(options)
