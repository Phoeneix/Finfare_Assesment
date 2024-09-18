'''Config data'''
from selenium.webdriver import Chrome
from utils.enums import ExecutionType


class Config():
    '''Config data'''

    # Selenium
    Driver:Chrome = None

    # Test step to skip
    Selected_Option:ExecutionType = ExecutionType.FULL

    # Temp storage
    Temp_List_Data:list = []