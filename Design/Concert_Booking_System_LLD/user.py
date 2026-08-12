# This class represents a user of the system
# A user can search concerts and book tickets

class User:

    def __init__(self, user_id, name, email, phone):

        # unique id for user
        self.user_id = user_id

        # user information
        self.name = name
        self.email = email
        self.phone = phone


    def get_user_id(self):
        return self.user_id
    
    def get_name(self):
        return self.get_name
    
    def get_email(self):
        return self.get_email
    
    def get_phone(self):
        return self.get_phone