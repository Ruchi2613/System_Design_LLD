from user import User

class WaitingList:
    def __init__(self):
        self.queue = []

    def add_user(self, user: User):
        self.queue.append(user)

    def next_user(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        return None