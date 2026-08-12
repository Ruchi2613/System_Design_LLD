from account import AccountTransaction
from card import Card
from banksystem import BankSystem
from cash_dispenser import CashDispenser

class ATM:

    def __init__(self, bank_system, cash_dispenser):
        self.bank_system = bank_system
        self.cash_dispenser = cash_dispenser

    def start(self, card):
        print("Welcome to the ATM!")
        card_number = card.card_number
        pin = card.pin

        account = self.bank_system.authenticate(card_number, pin)
        if not account:
            print("Invalid PIN")
            return

        print("Login Successful!")


        while True:
            print("\nPlease select an option:")
            print("1. Balance Check")
            print("2. Cash Withdrawal")
            print("3. Cash Deposit")
            print("4. Transaction History")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                balance = account.get_balance()
                print(f"Your current balance is: {balance}")
            elif choice == '2':
                # Aditya - You're checking that the ATM has money or not. 
                # If the ATM can dispense money, it will reduce the balance of ATM.
                # After that you check if your account has money or not. 
                # If your account then does not have money, then you dont withdraw it from your account.
                # But at this point you have already removed money from ATM
                # 
                # If ATM has money, then you try to withdraw from you bank,
                """
                Your Transactions should be be Atomic of ACID
                It either fully executes it or it doesn't

                Example:
                ATM has 1000
                Account has 200
                you want to withdraw 500

                then what your code does is - 
                ATM becomes 500 (as 500 removed from ATM)
                But 500 is > 200 - your balance. so you don;t withdraw from your account.

                but you already removed from the ATM lol
                """
                amount = int(input("Enter the amount to withdraw: "))
                if self.cash_dispenser.withdraw_cash(amount):
                    account.withdraw(amount)
                    print(f"Your new balance is: {account.get_balance()}")
            elif choice == '3':

                """
                Here you deposited in the ACCOUNT, but you added that money to the dispenser as well right.
                Example:

                ATM had 1000
                Your acc had 500

                you deposited 100
                your account became 600

                but you also added 100 to the ATM right so someone else can withdraw.
                so your ATM should also become 1100
                """

                amount = int(input("Enter the amount to deposit: "))
                account.deposit(amount)
                print(f"Your new balance is: {account.get_balance()}")
            elif choice == '4':
                print("Transaction History:")
                for transaction in account.get_transaction_history():
                    print(transaction)
            elif choice == '5':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")