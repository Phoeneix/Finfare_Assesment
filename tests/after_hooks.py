'''After test hooks'''
import config.config


# Local Variables
conf = config.config.Config

class AfterHooks():
    '''After test hooks class'''

    def AfterAll():
        conf.Driver.quit
