from card import Card
from account import AccountTransaction
from banksystem import BankSystem
from cash_dispenser import CashDispenser
from atm_machine import ATM

def main():
    # Bank system
    bank = BankSystem()

    # Account create
    account = AccountTransaction("12345", 10000, 1234)
    bank.add_account(account.account_number, account.balance, account.pin)

    # Card create
    card = Card("12345", "12/25", "123", 1234, "John Doe", "ABC Bank", "12345")

    # ATM + Cash
    dispenser = CashDispenser(50000)
    atm = ATM(bank, dispenser)

    # Start ATM
    atm.start(card)

if __name__ == "__main__":
    main()
    