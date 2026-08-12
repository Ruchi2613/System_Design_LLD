'''1. The car rental system should allow customers to browse and reserve available cars for specific dates.'''

from car_details import CarDetails
from car_data_enum import CarBrand, CarStatus,CarType, RentalLocation
from datetime import datetime, timedelta

class CheckAvailableCars:
    def __init__(self,cars: list[CarDetails],date:datetime,location:RentalLocation,days_required:int):
        self.cars = cars
        self.date = date
        self.location = location
        self.days_required = days_required


    def check_availability(self):
        available_cars = []
        end_date = self.date + timedelta(days=self.days_required)

        for car in self.cars:
            if car.get_status() != CarStatus.AVAILABLE:
                continue
            if car.get_location() != self.location:
                continue
            if not car.is_available(self.date, end_date):
                continue

            available_cars.append(car)

        return available_cars
        

    '''# Create some cars
car1 = CarDetails(
    brand=CarBrand.TOYOTA,
    model="Corolla",
    year=2022,
    license_plate="ABC123",
    rental_price_per_day=50,
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
    rental_price_per_day=45,
    type=CarType.SEDAN,
    available_date=datetime(2026, 4, 3),
    location=RentalLocation.AIRPORT,
    status=CarStatus.RENTED
)

car3 = CarDetails(
    brand=CarBrand.FORD,
    model="Explorer",
    year=2023,
    license_plate="FORD01",
    rental_price_per_day=80,
    type=CarType.SUV,
    available_date=datetime(2026, 4, 1),
    location=RentalLocation.DOWNTOWN,
    status=CarStatus.AVAILABLE
)


and Make a list of cars
cars_list = [car1, car2, car3]
This is the cars list that your CheckAvailableCars class expects.'''