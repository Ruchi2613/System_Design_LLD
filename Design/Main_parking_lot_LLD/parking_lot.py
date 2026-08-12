from parking_floor import ParkingFloor
from parking_ticket import ParkingTicket
from fee_strategy import FlatRateFeeStrategy, FeeStrategy
from parking_strategy import NearestFirstStrategy, ParkingStrategy
from vehicle import Vehicle
from typing import List, Dict, Optional


class ParkingLot:
    _instance = None

    def __init__(self):
        if ParkingLot._instance is not None:
            raise Exception("This class is a singleton!")
        self.floors: List[ParkingFloor] = []
        self.active_tickets: Dict[str, ParkingTicket] = {}
        self.fee_strategy = FlatRateFeeStrategy()
        self.parking_strategy = NearestFirstStrategy()

    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            ParkingLot._instance = ParkingLot()
        return ParkingLot._instance

    def add_floor(self, floor: ParkingFloor):
        self.floors.append(floor)

    def set_fee_strategy(self, fee_strategy: FeeStrategy):
        self.fee_strategy = fee_strategy

    def set_parking_strategy(self, parking_strategy: ParkingStrategy):
        self.parking_strategy = parking_strategy


    def park_vehicle(self, vehicle: Vehicle) -> Optional[ParkingTicket]:
        spot = self.parking_strategy.find_parking_spot(self.floors, vehicle)
        if spot is not None:
            spot.park_vehicle(vehicle)
            ticket = ParkingTicket(vehicle, spot)
            self.active_tickets[ticket.get_ticket_id()] = ticket
            print(f"Vehicle {vehicle.get_license_number()} parked at spot {spot.get_spot_id()}")
            return ticket
        else:
            print("No available parking spot for this vehicle.")
            return None
        

    def unpark_vehicle(self, license_number: str):
        ticket = self.active_tickets.pop(license_number, None)
        if ticket is None:
            print(f"Ticket not found for vehicle {license_number}")
            return None

        ticket.get_spot().unpark_vehicle()
        ticket.set_exit_timestamp()
        fee = self.fee_strategy.calculate_fee(ticket)
        print(f"Vehicle {license_number} unparked from spot {ticket.get_spot().get_spot_id()}")
        return fee
