from abc import ABC
from enum import Enum

# Define the VehicleSize enum inside the same file and Vehicle is a class that represents a real-world object (car, bike, truck) and uses VehicleSize as one of its properties to indicate the size of the vehicle. This allows us to categorize vehicles based on their size and potentially allocate parking spots accordingly.
class VehicleSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

# Define the Vehicle class as an abstract base class
class Vehicle(ABC):
    def __init__(self, license_number:str, size:VehicleSize):
        self.license_number = license_number
        self.size = size
    
    def get_license_number(self):
        return self.license_number
    
    def get_size(self):
        return self.size