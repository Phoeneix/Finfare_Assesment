'''Starter of the Test'''

import argparse
import sys

from pytest import Session
import pytest

import config.config
# import conftest
from tests.test_google import *
from utils.enums import ExecutionType


def ParseArguments():
    '''
    Parses the program arguments
    Returns
    -------
    args
    '''

    parser = argparse.ArgumentParser(
        description='Collect data from repositories and put it in a spreadsheet',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('-5', '--only5',
                        help='Execute the test with only step 5',
                        required=False,
                        action='store_true')

    parser.add_argument('-6', '--only6',
                        help='Execute the test with only step 6',
                        required=False,
                        action='store_true')

    parser.add_argument('-f', '--full',
                        help='Execute the test with only step 5',
                        required=False,
                        action='store_true')

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    '''
    The main executor
    '''

    args = ParseArguments()
    if args.only5:
        config.config.Config.Selected_Option = ExecutionType.ONLY5
        print(f'Test execution with only step 5 verification selected!')
    elif args.only6:
        config.config.Config.Selected_Option = ExecutionType.ONLY6
        print(f'Test execution with only step 6 verification selected!')
    else:
        config.config.Config.Selected_Option = ExecutionType.FULL
        print(f'Full execution selected!')

    exit_code = pytest.main(['-s'])
    if exit_code == 0:
        print('All tests passed!')
    else:
        print('Some tests failed.')
        print(f'Exit_code: "{exit_code}"')
        sys.exit(exit_code)

