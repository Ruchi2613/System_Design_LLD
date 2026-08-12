
import uuid
from collections import defaultdict
from FriendshipStatus import FriendshipStatus
from Request import Request    


class FriendshipService:

    def __init__(self):
        # Maps request_id -> FriendRequest object
        self.requests_by_id = {}
        # Maps user_id -> set of friend_user_ids
        self.user_friends = defaultdict(set)

    def send_friend_request(self, sender_id: str, receiver_id: str) -> Request:

        if sender_id == receiver_id:
            raise ValueError("Cannot send friend request to oneself.")

        if receiver_id in self.user_friends[sender_id]:
            raise ValueError("Users are already friends.")

        # Create unique ID for the request
        request_id = str(uuid.uuid4())

        # Create new request object (defaults to PENDING status)
        new_request = FriendRequest(sender_id=sender_id, receiver_id=receiver_id)

        # Save request to storage
        self.requests_by_id[request_id] = new_request

        print(f"Friend request sent from {sender_id} to {receiver_id}.")
        return request_id


    def respond_to_request(self, request_id: str, user_id: str, accept: bool):

        if request_id not in self.requests_by_id:
            raise ValueError("Request not found.")

        request = self.requests_by_id[request_id]

        if request.get_receiver_id() != user_id:
            raise ValueError("User is not the receiver of this request.")

        if accept == True:
            request.set_status(FriendshipStatus.ACCEPTED)
            # Add each other as friends
            self.user_friends[request.get_sender_id()].add(request.get_receiver_id())
            self.user_friends[request.get_receiver_id()].add(request.get_sender_id())
            print(f"Friend request {request_id} accepted.")
        else:
            request.set_status(FriendshipStatus.DECLINED)
            print(f"Friend request {request_id} declined.")


    
    def get_friends_list(self, user_id: str):
        return list(self.user_friends[user_id])

        