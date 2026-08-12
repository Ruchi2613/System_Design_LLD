'''1. The coffee vending machine should support different types of coffee, such as espresso, cappuccino, and latte.
'''

from enum import Enum

class CoffeeType(Enum):
    ESPRESSO = "espresso"
    AMERICANO = "americano"
    CAPPUCCINO = "cappuccino"
    LATTE = "latte"

'''2. Each type of coffee should have a specific price and recipe (ingredients and their quantities).'''
class CoffeeBean(Enum):
    ARABICA = "arabica"
    ROBUSTA = "robusta"
    LIBERICA = "liberica"
    EXCELSA = "excelsa"

class CoffeeSugar(Enum):
    WHITE_SUGAR = "white_sugar"
    BROWN_SUGAR = "brown_sugar"
    HONEY = "honey"
    STEVIA = "stevia"
    AGAVE = "agave"

class CoffeeMilk(Enum):
    WHOLE_MILK = "whole_milk"
    SKIM_MILK = "skim_milk"
    SOY_MILK = "soy_milk"
    ALMOND_MILK = "almond_milk"
    OAT_MILK = "oat_milk"

class SugarLevel(Enum):
    NO_SUGAR = "no_sugar"
    LOW_SUGAR = "low_sugar"
    MEDIUM_SUGAR = "medium_sugar"
    HIGH_SUGAR = "high_sugar"

class CoffeeStatus(Enum):
    IDLE = "idle"
    PREPARING = "preparing"
    READY = "ready"

class PaymentStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"

class PaymentMethod(Enum):
    CASH = "cash"
    CARD = "card"
    MOBILE_PAYMENT = "mobile_payment"

# class MachineStatus(Enum):
#     OPERATIONAL = "operational"
#     OUT_OF_ORDER = "out_of_order"
#     MAINTENANCE = "maintenance"

