import uuid
from UserData import UserData

class UserService:
    def __init__(self):

        # Storage dictionaries
        self.d_users_by_id = {}    # { user_id -> UserData object }
        self.d_credentials = {}    # { email -> password }
        self.email_to_id = {}      # { email -> user_id }


    def register_user(self, name:str, email:str, password:str, profile_picture_url:str = None, age:int = None, gender:str = None):
        # Check if email is already taken
        if email in self.d_credentials:
            raise ValueError("Email already registered.")

        if age is not None and age < 0 :
            raise ValueError("Invalid age.")

        if age is not None and age < 18 :
            raise ValueError("Should be 18+ to register.")

        self.d_credentials[email] = password  # Store credentials

        # Create new user
        new_user = UserData(name, email, profile_picture_url)
        user_id = new_user.get_user_id()

        # 2. Store in dictionaries
        self.d_credentials[email] = password
        self.email_to_id[email] = user_id             # Map email to user_id
        self.d_users_by_id[user_id] = new_user        # Map user_id to UserData


    def login(self, email:str, password:str):
        if email not in self.d_credentials or self.d_credentials[email] != password:
            raise ValueError("Invalid email or password.")


        user_id = self.email_to_id[email]
        user = self.d_users_by_id[user_id]

        print("Login successful for user:", user.get_name())
        return user_id


    '''You said: "We can't update user ID because it's generating every time."

You are 100% correct that user_id never changes! But update_profile needs user_id as a search key so the service knows WHICH user's profile in the dictionary to update!

Without passing user_id, UserService has no idea whose name to change:'''
    def update_profile(self, user_id: str, new_name: str = None, new_email: str = None, new_bio: str = None, new_profile_picture_url: str = None):
        # 1. Find the specific user object by ID
        if user_id not in self.d_users_by_id:
            raise ValueError("User not found.")
            # this
        user = self.d_users_by_id[user_id]

        # 2. Call the setters from UserData! (Solves Question 3)
        if new_name is not None:
            user.update_name(new_name)
            
        if new_email is not None:
            # 1. Get current email and password
            old_email = user.get_email()
            password = self.d_credentials[old_email]  # Save the password!
            
            # 2. Delete old email entries
            del self.d_credentials[old_email]
            del self.email_to_id[old_email]
            
            # 3. Update the UserData object
            user.update_email(new_email)
            
            # 4. Store new email in both dictionaries
            self.email_to_id[new_email] = user_id
            self.d_credentials[new_email] = password  # Restore the password

        if new_bio is not None:
            user.update_bio(new_bio)
            
        if new_profile_picture_url is not None:
            user.update_profile_picture_url(new_profile_picture_url)

        print(f"Profile updated successfully for user {user.get_name()}!")