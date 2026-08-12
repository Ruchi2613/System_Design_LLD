'''## Requirements
1. The ATM system should support basic operations such as balance inquiry, cash withdrawal, and cash deposit.
2. Users should be able to authenticate themselves using a card and a PIN (Personal Identification Number).
3. The system should interact with a bank's backend system to validate user accounts and perform transactions.
4. The ATM should have a cash dispenser to dispense cash to users.'''

class Card:
    def __init__(self, card_number, expiry_date, cvv, pin, holder_name, bank_name, account_number):
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv
        self.pin = pin
        self.holder_name = holder_name
        '''bank_name is the name of the bank that issued the card.'''
        self.bank_name = bank_name
        '''account_number is the unique identifier for the user's bank account associated with this card.'''
        self.account_number = account_number 

    def validate_pin(self, input_pin):
        return self.pin == input_pin
    