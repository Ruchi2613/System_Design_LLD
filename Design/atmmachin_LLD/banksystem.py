from account import AccountTransaction

class BankSystem:
    def __init__(self):
        '''accounts is a dictionary that stores the account information for each user. The keys are the account numbers, and the values are instances of the AccountTransaction class.'''
        self.accounts = {}

    def add_account(self, account_number, balance, pin):
        self.accounts[account_number] = AccountTransaction(account_number, balance, pin)

    def get_account(self, account_number):
        '''get_account method retrieves the account information for a given account number. It returns the corresponding AccountTransaction instance if the account exists, or None if it does not.'''
        return self.accounts.get(account_number)

    
    def authenticate(self, account_number, pin):
        '''authenticate method verifies the user's identity by checking the provided account number and PIN against the stored account information. It returns the AccountTransaction instance if authentication is successful, or None if it fails.'''
        account = self.get_account(account_number)
        if account and account.check_pin(pin):
            return account
        return None

    '''accounts = {
    "12345": <AccountTransaction object>,
    "67890": <AccountTransaction object>,
    ...
}


So conceptually:

accounts = {
    "12345": <AccountTransaction object>,
    "67890": <AccountTransaction object>,
    ...
}


2. add_account function takes an account number and a balance, creates a new AccountTransaction object, and stores it in the accounts dictionary with the account number as the key. For example:
self.accounts[account_number] = AccountTransaction(account_number, balance)

Step by step:

You call add_account("12345", 10000).
Python creates a new object of AccountTransaction:
acc_obj = AccountTransaction("12345", 10000)
---

acc_obj = AccountTransaction("12345", 10000)
Now acc_obj is an object that stores:
acc_obj.account_number = "12345"
acc_obj.balance = 10000
Python then adds it to the accounts dictionary:
self.accounts["12345"] = 


Now the dictionary looks like:

{
    "12345": <AccountTransaction object with balance 10000>
}

get_account process
acc = self.accounts.get("12345")
Python looks in the dictionary for the key "12345".
If it exists → returns the value, which is the AccountTransaction object.
You can now access object attributes:
print(acc.account_number)  # 12345
print(acc.balance)         # 10000'''