'''## Requirements
1. The ATM system should support basic operations such as balance inquiry, cash withdrawal, and cash deposit.
2. Users should be able to authenticate themselves using a card and a PIN (Personal Identification Number).
3. The system should interact with a bank's backend system to validate user accounts and perform transactions.
4. The ATM should have a cash dispenser to dispense cash to users.'''

class CashDispenser:
    def __init__(self, balance):
        '''balance is the amount of cash available in the dispenser.'''
        self.balance = balance

    def withdraw_cash(self, amount):
        '''withdraw_cash method allows the user to withdraw cash from the dispenser. It takes an amount as input and checks if the dispenser has enough cash to fulfill the request. If it does, it dispenses the cash and updates the balance accordingly.'''
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f'You have withdrawn: {amount}')
            return f'after withdrawing your current balance in dispenser is: {self.balance}'
        else:
            return f"Insufficient cash in dispenser or invalid amount."
        
    def get_balance(self):
        '''get_balance method returns the current balance of cash available in the dispenser.'''
        return self.balance
