from enum import Enum

class seatTypes(Enum):
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"


class seatAvailableStatus(Enum):
    AVAILABLE = "AVAILABLE"
    RESERVED = "RESERVED"