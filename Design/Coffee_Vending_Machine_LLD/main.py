from coffe_type_enum import CoffeeType, PaymentMethod, PaymentStatus
from ingredient import EspressoRecipe, CappuccinoRecipe, LatteRecipe
from payment import Payment
from menu import CoffeeMenu

coffee1 = EspressoRecipe()
coffee1.prepare_ingredients("whole_milk", "white_sugar", "arabica")
coffee1.making_coffee()
coffee1.serve_coffee()

coffee2 = CappuccinoRecipe()
coffee2.prepare_ingredients("skim_milk", "brown_sugar", "robusta")
coffee2.making_coffee()
coffee2.serve_coffee()

coffee3 = LatteRecipe()
coffee3.prepare_ingredients("soy_milk", "honey", "liberica")
coffee3.making_coffee()
coffee3.serve_coffee()

coffees_list = [coffee1, coffee2, coffee3]

menu = CoffeeMenu()
menu.display_menu()

selected_coffee = coffees_list[0]

print("\nSelected Coffee:")
print(selected_coffee)

coffee_type_map = {
    coffee1: CoffeeType.ESPRESSO,
    coffee2: CoffeeType.CAPPUCCINO,
    coffee3: CoffeeType.LATTE
}

selected_coffee_type = coffee_type_map[selected_coffee]

price = menu.menu[selected_coffee_type.value]

payment = Payment(price, PaymentMethod.CARD)
payment.process_payment()

if payment.get_status() == PaymentStatus.COMPLETED:
    print("\nPayment Successful")
    print(f"{selected_coffee_type.value} is ready! Enjoy your coffee ☕")
else:
    print("\nPayment Failed")