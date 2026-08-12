'''2. Each car should have details such as brand, model, year, license plate number, and rental price per day.
'''

from car_data_enum import CarBrand,RentalLocation,CarStatus,CarType,RentalDuration
from datetime import datetime

class CarDetails:
    def __init__(self, brand:CarBrand, model, year, license_plate, rental_price_per_day,type:CarType, available_date:datetime, location:RentalLocation, status:CarStatus):
        self.brand = brand
        self.model = model
        self.year = year
        self.license_plate = license_plate
        self.rental_price_per_day = rental_price_per_day
        self.available_date = available_date
        self.location = location
        self.status = status
        self.type = type


        self.reservations = []

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_license_plate(self):
        return self.license_plate

    def get_rental_price_per_day(self):
        return self.rental_price_per_day
    
    def get_location(self):
        return self.location

    def get_status(self):
        return self.status

    def get_available_date(self):
        return self.available_date
    
    def get_type(self):
        return self.type
    

    def car_info(self):
        return f"Brand: {self.brand.value}, Model: {self.model}, Year: {self.year}, " \
           f"License Plate: {self.license_plate}, Price/Day: {self.rental_price_per_day}, " \
           f"Type: {self.type.value}, Status: {self.status.value}, Location: {self.location.value}"
    

    def calculate_rental_cost(self, duration: RentalDuration, days: int):
        DURATION_DAYS = {
            RentalDuration.ONE_DAY: 1,
            RentalDuration.WEEKLY: 7,
            RentalDuration.MONTHLY: 30
        }

        if duration in DURATION_DAYS:
            days = DURATION_DAYS[duration]
        if days is None:
            days = 1

        return self.rental_price_per_day * days
    

    def is_available(self, requested_start, requested_end):
        for booking in self.reservations:
            if not (requested_end <= booking["start"] or requested_start >= booking["end"]):
                return False
        return True


    def add_reservation(self, start, end):
        if self.is_available(start, end):
            self.reservations.append({"start": start, "end": end})
            return True
        return False
    
    '''self.reservations = [
    {"start": April 5, "end": April 10},
    {"start": April 12, "end": April 15}
]'''
    