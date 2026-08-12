from abc import ABC, abstractmethod
from parking_floor import ParkingFloor
from vehicle import Vehicle, VehicleSize
from parking_spot import ParkingSpot
from typing import List, Optional

class ParkingStrategy(ABC):
    @abstractmethod
    def find_parking_spot(self, floors: List[ParkingFloor], vehicle: Vehicle) -> Optional[ParkingSpot]:
        pass

class NearestFirstStrategy(ParkingStrategy):
    def find_parking_spot(self, floors: List[ParkingFloor], vehicle: Vehicle) -> Optional[ParkingSpot]:
        for floor in floors:
            spot = floor.find_available_spot(vehicle)
            if spot is not None:
                return spot
        return None
    


class FarthestFirstStrategy(ParkingStrategy):
    def find_parking_spot(self, floors: List[ParkingFloor], vehicle: Vehicle) -> Optional[ParkingSpot]:
        for floor in reversed(floors):
            spot = floor.find_available_spot(vehicle)
            if spot is not None:
                return spot
        return None
    

class RandomStrategy(ParkingStrategy):
    def find_parking_spot(self, floors: List[ParkingFloor], vehicle: Vehicle) -> Optional[ParkingSpot]:
        import random
        random_floors = random.sample(floors, len(floors))
        for floor in random_floors:
            spot = floor.find_available_spot(vehicle)
            if spot is not None:
                return spot
        return None
    
