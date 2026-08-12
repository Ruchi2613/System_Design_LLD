class parkingLot:
    def __init__(self):
        self.total_spots = []
    
    def add_parking_spot(self,spot):
        self.total_spots.append(spot)

    def find_available_spot(self, vehicle):
        for spot in self.total_spots:
            if spot.is_occupied == False:
                spot.is_occupied = True
                spot.vehicle = vehicle
                print(f"Vehicle {vehicle.license_number} parked at spot {spot.spot_id}")
                return spot
        print("No available parking spots.")
        return None
    
    def remove_vehicle(self, license_number):
        for spot in self.total_spots:
            if spot.is_occupied and spot.vehicle.license_number == license_number: # where it checks if the spot is occupied and if the vehicle's license number matches the one provided so it checks from the parking lot's total spots and if it finds a match it marks the spot as unoccupied and removes the vehicle from that spot
                spot.is_occupied = False
                spot.vehicle = None
                print(f"Vehicle {license_number} left the parking spot {spot.spot_id}")
                return spot
        print(f"Vehicle {license_number} not found.")
        return False


if __name__ == "__main__":
    from parkingspot import parkingSpot
    from vehicle import Vehicle

    
    spot1 = parkingSpot(1)
    spot2 = parkingSpot(2)

    car1 = Vehicle("ABC123") # where we create two parking spots and two vehicles with different license numbers. We then create a parking lot and add the parking spots to it. We find available spots for both vehicles and then remove one of the vehicles from the parking lot using its license number.
    car2 = Vehicle("XYZ789")


    parking_lot = parkingLot()
    parking_lot.add_parking_spot(spot1)
    parking_lot.add_parking_spot(spot2) # it looks like this in list = [spot1, spot2]

    parking_lot.find_available_spot(car1) # it takes the license number as vehicle and finds an available spot for car1
    parking_lot.find_available_spot(car2) # it takes the license number as vehicle and finds an available spot for car2

    parking_lot.remove_vehicle("ABC123")
