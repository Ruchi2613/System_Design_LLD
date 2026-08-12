from enum import Enum

class FriendshipStatus(Enum):
    PENDING = "PENDING" # Request sent, waiting for receiver to respond
    ACCEPTED = "ACCEPTED" # Both users are now friends
    BLOCKED = "BLOCKED" # Receiver rejected the request
    DECLINED = "DECLINED"  # One user blocked the other