from vehicle import Vehicle, VehicleSize

class Truck(Vehicle):
    def __init__(self, license_number: str):
        super().__init__(license_number, VehicleSize.LARGE)