'''Config data'''

from utils.enums import ExecutionType


class Config():
    '''Config data'''

    # Selenium
    Driver = None

    # Test step to skip
    Selected_Option:ExecutionType = ExecutionType.FULL
