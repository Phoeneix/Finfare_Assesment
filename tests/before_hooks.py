'''Before test hooks'''
import config.config


# Local Variables
conf = config.config.Config

class BeforeHooks():
    '''Before test hooks class'''

    def BeforeTest():
        conf.Driver = new Chromedriver()
