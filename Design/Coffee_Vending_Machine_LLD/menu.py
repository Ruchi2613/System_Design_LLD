'''3. The machine should have a menu to display the available coffee options and their prices.
'''
class CoffeeMenu:
    def __init__(self):
        self.menu = {
            "espresso": 2.5,
            "cappuccino": 3.0,
            "latte": 3.5
        }

    def display_menu(self):
        print("Coffee Menu:")
        for coffee, price in self.menu.items():
            print(f"{coffee}: ${price:.2f}")
