from enum import Enum

# class CarBrand(Enum):
#     TOYOTA = "Toyota",
#     HONDA = "Honda",
#     FORD = "Ford",
#     BMW = "BMW",
#     MERCEDES_BENZ = "Mercedes-Benz",
#     AUDI = "Audi",
#     VOLKSWAGEN = "Volkswagen",

'''Note: , is used to separate the values in the enum, and each value is a tuple containing a single string.
which looks like this: print(CarBrand.TOYOTA.value)  # Output: ('Toyota',)'''


class CarBrand(Enum):
    TOYOTA = "Toyota"
    HONDA = "Honda"
    FORD = "Ford"
    BMW = "BMW"
    MERCEDES_BENZ = "Mercedes-Benz"
    AUDI = "Audi"
    VOLKSWAGEN = "Volkswagen"


'''Now each enum member’s value is a string, as intended. You can access the value of an enum member like this:
print(CarBrand.TOYOTA.value)  # Output: "Toyota"'''


class CarType(Enum):
    SEDAN = "Sedan"
    SUV = "SUV"
    CONVERTIBLE = "Convertible"
    COUPE = "Coupe"
    MINIVAN = "Minivan"
    PICKUP = "Pickup"


class CarStatus(Enum):
    AVAILABLE = "Available"
    RENTED = "Rented"
    MAINTENANCE = "Maintenance"


class PriceCategory(Enum):
    ECONOMY = "Economy"
    STANDARD = "Standard"
    LUXURY = "Luxury"


class RentalDuration(Enum):
    ONE_DAY = "One Day"
    WEEKLY = "Weekly"
    MONTHLY = "Monthly"

class RentalLocation(Enum):
    DOWNTOWN = "Downtown"
    AIRPORT = "Airport"
    SUBURBAN = "Suburban"

class PaymentMethod(Enum):
    CREDIT_CARD = "Credit Card"
    DEBIT_CARD = "Debit Card"
    CASH = "Cash"
    MOBILE_PAYMENT = "Mobile Payment"

class PaymentStatus(Enum):
    PENDING = "Pending"
    SUCCESS = "Success"
    FAILED = "Failed"



'''Enum	Meaning / Use Case:

SEDAN	Standard 4-door car, comfortable for 4–5 people, good for city/highway driving.
SUV	Sport Utility Vehicle, bigger, more cargo space, can handle rougher roads.
CONVERTIBLE	Car with a roof that can be folded down, stylish and fun to drive, usually 2–4 seats.
COUPE	Sporty 2-door car, usually for style and speed rather than passengers.
MINIVAN	Big van, designed to carry 6–8 people, good for family trips.
PICKUP	Truck with cargo bed in the back, useful for hauling goods or off-road driving.'''