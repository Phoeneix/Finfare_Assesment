'''Enum for execution types'''
from enum import Enum


class ExecutionType(Enum):
    '''Execution type Enum'''

    FULL = 1
    NO_VERIFICATION = 2
    ONLY5 = 3
    ONLY6 = 4

    @staticmethod
    def FromStr(label):
        '''Method to turn string into the Enum'''

        if label.lower() in ['only5']:
            return ExecutionType.ONLY5
        if label.lower() in ['only6']:
            return ExecutionType.ONLY6
        if label.lower() in ['v','skip_verification']:
            return ExecutionType.NO_VERIFICATION
        if label.lower() in ['full', 'f']:
            return ExecutionType.FULL
        raise NotImplementedError(f'Execution type for "{label}" is not implemented!')
