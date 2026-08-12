from ast import Dict
from collections import defaultdict
from parking_spot import ParkingSpot
from vehicle import VehicleSize,Vehicle


class ParkingFloor:
    def __init__(self, floor_number):
        self.floor_number = floor_number
        self.spots: Dict[str, ParkingSpot] = {}  # Key → string (spot_id) Value → ParkingSpot object
    # where we initialize the parking floor with a floor number and an empty dictionary to hold the parking spots on that floor. The keys of the dictionary are the spot IDs and the values are instances of the ParkingSpot class.
    # dict looks like this  = self.spots = {
    #     "F1-S1": ParkingSpot("F1-S1", VehicleSize.SMALL),
    #     "F1-M1": ParkingSpot("F1-M1", VehicleSize.MEDIUM),
    #     "F2-L1": ParkingSpot("F2-L1", VehicleSize.LARGE)
    # }

    def add_spot(self, spot: ParkingSpot):
        self.spots[spot.get_spot_id()] = spot  # self.spots["F1-S1"] = spot1 object loc i.e; <ParkingSpot object at 0x123>

        # self.spots = {
#     "F1-S1": <ParkingSpot object at 0x123>,
#     "F1-M1": <ParkingSpot object at 0x456>
# }


    # it looks like this = vehicle = Vehicle("KA-01-1234", VehicleSize.SMALL)
                        # floor.find_available_spot(vehicle)
    def find_available_spot(self, vehicle: Vehicle):
        available_spots = []
        for spot_val in self.spots.values():  # self.spots.values() have = [spot1_object, spot2_object, spot3_object]
            if spot_val.is_occupied == False and spot_val.can_fit_vehicle(vehicle)==True:
                available_spots.append(spot_val)
        if available_spots != []:
            available_spots.sort(key=lambda x: x.get_spot_size().value)
            return available_spots[0]
        return None
    

    def display_availability(self):
        print(f"--- Floor {self.floor_number} Availability ---")
        available_counts = defaultdict(int)
        
        for spot in self.spots.values():
            if not spot.is_occupied_spot():
                available_counts[spot.get_spot_size()] += 1

        for size in VehicleSize:
            print(f"  {size.value} spots: {available_counts[size]}")