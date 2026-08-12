from datetime import datetime, timedelta

from car_details import CarDetails
from check_avail_cars import CheckAvailableCars
from payment import Payment

from car_data_enum import CarBrand, CarType, CarStatus, RentalLocation,PaymentMethod



car1 = CarDetails(
    brand=CarBrand.TOYOTA,
    model="Corolla",
    year=2022,
    license_plate="ABC123",
    rental_price_per_day=80,
    type=CarType.SEDAN,
    available_date=datetime(2026, 4, 2),
    location=RentalLocation.DOWNTOWN,
    status=CarStatus.AVAILABLE
)

car2 = CarDetails(
    brand=CarBrand.HONDA,
    model="Civic",
    year=2021,
    license_plate="XYZ789",
    rental_price_per_day=60,
    type=CarType.SEDAN,
    available_date=datetime(2026, 4, 2),
    location=RentalLocation.AIRPORT,
    status=CarStatus.AVAILABLE
)

car3 = CarDetails(
    brand=CarBrand.FORD,
    model="Explorer",
    year=2023,
    license_plate="FORD01",
    rental_price_per_day=120,
    type=CarType.SUV,
    available_date=datetime(2026, 4, 2),
    location=RentalLocation.DOWNTOWN,
    status=CarStatus.AVAILABLE
)

cars_list = [car1, car2, car3]

search_date = datetime(2026, 4, 2)
location = RentalLocation.DOWNTOWN
days_required = 3

checker = CheckAvailableCars(cars_list, search_date, location, days_required)

available_cars = checker.check_availability()

print("\nAvailable Cars:")
for car in available_cars:
    print(car.car_info())

selected_car = available_cars[0]  

print("\nSelected Car:")
print(selected_car.car_info())


start_date = search_date
end_date = start_date + timedelta(days_required)

if selected_car.add_reservation(start_date, end_date):
    print("\nReservation Successful")


    total_cost = selected_car.calculate_rental_cost(location, days_required)
    print(f"Total Cost: ${total_cost}")

    
    payment = Payment(total_cost, PaymentMethod.CREDIT_CARD)

    payment.process_payment()

    if payment.get_payment_status().value == "Success":
        print("Payment Successful")
        print("Booking Confirmed")
    else:
        print("Payment Failed")

else:
    print("Car not available for selected dates")