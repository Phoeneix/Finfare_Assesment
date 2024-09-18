'''The test steps'''

import config.config
from pages.google_finance_page import GoogleFinancePage
from utils.enums import ExecutionType


# Local Variables
conf = config.config.Config

@Test
def GoogleFinanceTest():

    test_data = ["NFLX","MSFT", "TSLA"]

    # 1. Opens a webpage www.google.com/finance on a chrome browser
    conf.Driver.new('http://www.google.com/finance')

    # 2. Verifies the page is loaded by asserting the page title
    is_loaded = GoogleFinancePage.WaitForPageToLoad(timeout = 10)
    assert is_loaded, f'Page "{GoogleFinancePage.Name}" did not load!'

    # 3. Retrieves the stock symbols listed under the section “You may be interested in info”
    stock_symbols_present = GoogleFinancePage.GetSymbolList()

    # 4. Compare the stock symbols retrieved from (3) with given test data
    not_in_present = test_data
    not_in_test_data = []
    for stock_symbol in stock_symbols_present:
        if stock_symbol in test_data:
            not_in_present.remove(stock_symbol)
        else:
            not_in_test_data.append(stock_symbol)

    # 5. Print all stock symbols that are in (3) but not in given test data
    if conf.Selected_Option in [ExecutionType.ONLY5, ExecutionType.FULL]:
        print('Symbols on the page that not present in the provided test data:')
        for stock_symbol in not_in_test_data:
            print(stock_symbol)

    # 6. Print all stock symbols that are in given test data but not in (3)
    if conf.Selected_Option in [ExecutionType.ONLY6, ExecutionType.FULL]:
        print('Symbols not present on the page but present in the provided test data:')
        for stock_symbol in not_in_present:
            print(stock_symbol)
