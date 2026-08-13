from datetime import datetime


class AccountService:

    def __init__(self):
        # local db as a dictionary to store user data
        self.local_db = {}

    def sign_up(self,un,password,confirm_password,email,phone_number,created_at=None):
        self.username = un
        self.password = password
        self.confirm_password = confirm_password
        self.email = email
        self.phone_number = phone_number
        self.created_at = created_at

        if (
            not self.username
            or not self.password
            or not self.confirm_password
            or not self.email
            or not self.phone_number
        ):
            raise ValueError("All fields are required.")

        if len(self.password) < 8:
            raise ValueError("Password must be at least 8 characters long.")

        hashed_password = hash(self.password)
        hashed_confirm_password = hash(self.confirm_password)

        if hashed_password != hashed_confirm_password:
            raise ValueError("Passwords do not match.")

        for key, value in self.local_db.items():
            if self.phone_number == value["phone_number"]:
                raise ValueError("Phone number already exists.")

            if self.email == value["email"]:
                raise ValueError("Email already exists.")

            if self.username == key:
                raise ValueError("Username already exists.")

        self.local_db[self.username] = {
            "password": hashed_password,
            "email": self.email,
            "phone_number": self.phone_number,
            "created_at": self.created_at,
        }

        print("User registered successfully.")
        return True

    def signIn(self, username, password):

        if username not in self.local_db:
            raise ValueError("Username does not exist")

        hashed_password = hash(password)

        if self.local_db[username]["password"] != hashed_password:
            raise ValueError("Incorrect password")

        print("User signed in successfully.")
        return True