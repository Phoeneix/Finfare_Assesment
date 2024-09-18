'''The test steps'''

import config.config
from pages.google_finance_page import GoogleFinancePage
from utils.enums import ExecutionType


# Local Variables
conf = config.config.Config

def test_google_finance():

    test_data = ["NFLX","MSFT", "TSLA"]

    # 1. Opens a webpage www.google.com/finance on a chrome browser
    conf.Driver.get('http://www.google.com/finance')

    # 2. Verifies the page is loaded by asserting the page title
    is_loaded = GoogleFinancePage.WaitForPageToLoad(timeout = 10)
    assert is_loaded, f'Page "{GoogleFinancePage.Name}" did not load!'

    # 3. Retrieves the stock symbols listed under the section “You may be interested in info”
    stock_symbols_present = GoogleFinancePage.GetSymbolList()

    # 4. Compare the stock symbols retrieved from (3) with given test data
    if stock_symbols_present != test_data:
       print(f'The stock symbols on the webpage "{stock_symbols_present}" are not matching the expected list "{test_data}"')
    else:
        print('All expected symbol is on the page!')

    # 5. Print all stock symbols that are in (3) but not in given test data
    if conf.Selected_Option in [ExecutionType.ONLY5, ExecutionType.FULL]:
        print('\r\nSymbols on the page that are not expected:')
        for stock_symbol in stock_symbols_present:
            if stock_symbol not in test_data:
                print(stock_symbol)

    # 6. Print all stock symbols that are in given test data but not in (3)
    if conf.Selected_Option in [ExecutionType.ONLY6, ExecutionType.FULL]:
        print('\r\nSymbols not present on the page but are expected:')
        for stock_symbol in test_data:
            if stock_symbol not in stock_symbols_present:
                print(stock_symbol)
