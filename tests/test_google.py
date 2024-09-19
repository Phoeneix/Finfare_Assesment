'''The test steps'''

import config.config
from pages.google_finance_page import GoogleFinancePage
from utils.enums import ExecutionType


# Local Variables
conf = config.config.Config
test_data = ["NFLX","MSFT", "TSLA"]

def test_open_page_in_chrome():
    # 1. Opens a webpage www.google.com/finance on a chrome browser
    print('\n\n======== Step 1. - Opens a webpage www.google.com/finance on a chrome browser ========')
    print(f'\nDriver: {conf.Driver}')
    conf.Driver.get('http://www.google.com/finance')


def test_check_if_page_loaded():
    # 2. Verifies the page is loaded by asserting the page title
    print('\n\n======== Step 2. - Verifies the page is loaded by asserting the page title ========')
    google_finance_page = GoogleFinancePage()
    is_loaded = google_finance_page.WaitForPageToLoad(timeout = 10)
    print(f'\nPage Name: {google_finance_page.page_name}')
    print(f'Is page loaded: {is_loaded}')
    assert is_loaded, f'Page "{google_finance_page.page_name}" did not load!'


def test_read_stock_symbols():
    # 3. Retrieves the stock symbols listed under the section "You may be interested in info"
    print('\n\n======== Step 3. - Retrieves the stock symbols listed under the section "You may be interested in info ========')
    google_finance_page = GoogleFinancePage()
    conf.Temp_List_Data = google_finance_page.GetSymbolList()
    print(f'\nSymbols: {conf.Temp_List_Data}')


def test_compare_symbols():
    # 4. Compare the stock symbols retrieved from (3) with given test data
    print('\n\n======== Step 4. - Compare the stock symbols retrieved from (3) with given test data "["NFLX","MSFT", "TSLA"]" ========')
    stock_symbols_present = conf.Temp_List_Data
    print(f'\nSymbols equal with test data: {stock_symbols_present == test_data}')
    print(f'Symbols: {stock_symbols_present}')
    print(f'Test Data: {test_data}')
    assert stock_symbols_present == test_data,  f'The stock symbols on the webpage "{stock_symbols_present}" are not matching the expected list "{test_data}"'


def test_print_extra_symbols():
    # 5. Print all stock symbols that are in (3) but not in given test data
    print('\n\n======== Step 5. - Print all stock symbols that are in (3) but not in given test data ========')
    if conf.Selected_Option in [ExecutionType.ONLY5, ExecutionType.FULL]:
        print('\nSymbols on the page that are not expected:')
        stock_symbols_present = conf.Temp_List_Data
        for stock_symbol in stock_symbols_present:
            if stock_symbol not in test_data:
                print(stock_symbol)
    else:
        print('\nSkipped...')


def test_print_missing_symbols():
    # 6. Print all stock symbols that are in given test data but not in (3)
    print('\n\n======== Step 6. - Print all stock symbols that are in given test data but not in (3) ========')
    if conf.Selected_Option in [ExecutionType.ONLY6, ExecutionType.FULL]:
        print('\nSymbols not present on the page but are expected:')
        stock_symbols_present = conf.Temp_List_Data
        for stock_symbol in test_data:
            if stock_symbol not in stock_symbols_present:
                print(stock_symbol)
    else:
        print('\nSkipped...')
