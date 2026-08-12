from enum import Enum

class Way(Enum):
    ONE_WAY = "ONE_WAY"
    ROUND_TRIP = "ROUND_TRIP"

    '''Note: Python variable names cannot start with number or contain - like 1-way '''