class parkingSpot:
    def __init__(self,spot_id):
        self.spot_id = spot_id
        self.is_occupied = False
        self.vehicle = None

# This class represents a single parking spot
# It keeps track of the vehicle parked in the spot and its occupancy status
