'''Enum for execution types'''
from enum import Enum


class ExecutionType(Enum):
    '''Execution type Enum'''

    FULL = 1
    ONLY5 = 2
    ONLY6 = 2

    @staticmethod
    def FromStr(label):
        '''Method to turn string into the Enum'''

        if label.lower() in ['only5']:
            return ExecutionType.ONLY5
        if label.lower() in ['only6']:
            return ExecutionType.ONLY6
        if label.lower() in ['full', 'f']:
            return ExecutionType.FULL
        raise NotImplementedError(f'Execution type for "{label}" is not implemented!')
