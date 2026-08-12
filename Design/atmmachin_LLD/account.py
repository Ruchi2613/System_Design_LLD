'''## Requirements
1. The ATM system should support basic operations such as balance inquiry, cash withdrawal, and cash deposit.
2. Users should be able to authenticate themselves using a card and a PIN (Personal Identification Number).
3. The system should interact with a bank's backend system to validate user accounts and perform transactions.
4. The ATM should have a cash dispenser to dispense cash to users.'''

'''user of account can perform operations like balance inquiry, cash withdrawal, and cash deposit.'''
class AccountTransaction:
    '''account_number is the unique identifier for the user's bank account'''
    '''balance is the current amount of money in the user's bank account.'''
    def __init__(self, account_number, balance, pin):
        self.account_number = account_number
        self.balance = balance
        self.pin = pin
        self.transaction_history = []

    def deposit(self, amount):
        '''deposit method allows the user to add money to their account. It takes an amount as input and adds it to the current balance.'''
        self.balance += amount
        self.transaction_history.append(("deposit", amount))
        return self.balance


    def withdraw(self, amount):
        '''withdraw method allows the user to remove money from their account. It takes an amount as input and subtracts it from the current balance.'''
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(("withdraw", amount))
            return f'after withdrawing your current balance is: {self.balance}'
        else:
            return f"Insufficient balance or invalid amount."

    def get_balance(self):
        '''get_balance method returns the current balance of the user's account.'''
        return self.balance
    
    def check_pin(self, pin):
        '''check_pin method verifies if the provided PIN matches the stored PIN for the account.'''
        return self.pin == pin
    
    def get_transaction_history(self):
        '''get_transaction_history method returns a list of all transactions made on the account.'''
        return self.transaction_history
