from vehicle import Vehicle, VehicleSize

class Car(Vehicle):
    def __init__(self, license_number: str):
        super().__init__(license_number, VehicleSize.MEDIUM)