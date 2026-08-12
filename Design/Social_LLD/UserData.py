import uuid

class UserData:
    def __init__(self, name: str, email: str, profile_picture_url: str = None):
        # Immutable / Unchanging ID
        self.user_id = str(uuid.uuid4())  # Auto-generates unique ID

        # Profile fields
        self.name = name
        self.email = email
        self.bio = ""                     # Starts empty
        self.profile_picture_url = profile_picture_url

    # Getters
    def get_user_id(self):
        return self.user_id
    
    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email

    def get_bio(self):
        return self.bio

    def get_profile_picture_url(self):
        return self.profile_picture_url

    # Setters
    def update_name(self, new_name: str):
        self.name = new_name

    def update_email(self, new_email: str):
        self.email = new_email

    def update_bio(self, new_bio: str):
        self.bio = new_bio

    def update_profile_picture_url(self, new_profile_picture_url: str):
        self.profile_picture_url = new_profile_picture_url

'''Constructor  ──>  Creates the object with initial values (Happens ONCE)
Setter       ──>  Updates values later on as things change (Happens ANY TIME)
If a user signs up today, you pass their initial info into the constructor:

Python
user = UserData("u123", "Alice", "alice@email.com", "123-456-7890")
What happens 6 months from now when Alice changes her email address or updates her profile picture?

Without a way to update it, user.email stays stuck as "alice@email.com".

You don't want to create a whole new UserData object from scratch just to change one email! That's where a setter (or updating the attribute) comes in.'''