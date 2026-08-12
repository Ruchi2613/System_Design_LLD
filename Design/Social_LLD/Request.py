# [ Request ] ─> Sender ID, Receiver ID, Status (PENDING)
from datetime import datetime
from FriendshipStatus import FriendshipStatus

class Request:
    def __init__(self, sender_id: str, receiver_id: str, status: FriendshipStatus = FriendshipStatus.PENDING, created_at: datetime   None):
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        # Automatically defaults to PENDING!
        self.status = status
        self.created_at = created_at if created_at else datetime.now()

    def get_sender_id(self):
        return self.sender_id

    def get_receiver_id(self):
        return self.receiver_id

    def get_status(self):
        return self.status

    def get_created_at(self):
        return self.created_at

    # Setter (Crucial for updating state!)
    def set_status(self, new_status:FriendshipStatus):
        self.status = new_status
