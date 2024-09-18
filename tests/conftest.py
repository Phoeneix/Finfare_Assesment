from selenium.webdriver import Chrome, ChromeOptions

import config.config


# Local Variables
conf = config.config.Config

def pytest_sessionstart(session):
    print('\n\nExecuting before all hook...\n')
    options = ChromeOptions()
    options.add_argument('--headless')
    conf.Driver = Chrome(options)


def pytest_sessionfinish(session):
    print('\n\nExecuting after all hook...\n')
    conf.Driver.quit