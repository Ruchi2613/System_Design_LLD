from abc import ABC, abstractmethod
from vehicle import VehicleSize,Vehicle
from parking_ticket import ParkingTicket


class FeeStrategy(ABC):
    @abstractmethod
    def calculate_fee(self, parking_ticket: ParkingTicket) -> float:
        pass

class FlatRateFeeStrategy(FeeStrategy):
    RATE_PER_HOUR = 1.0

    def calculate_fee(self, parking_ticket: ParkingTicket) -> float:
        duration = parking_ticket.get_exit_timestamp() - parking_ticket.get_entry_timestamp()
        hours = (duration // (1000 * 60 * 60)) + 1  # 1000 milliseconds = 1 second, 60 seconds = 1 minute, 60 minutes = 1 hour
        return self.RATE_PER_HOUR * hours
    

class VehicleBasedFeeStrategy(FeeStrategy):
    HOURLY_RATES = {
        VehicleSize.SMALL: 1.0,
        VehicleSize.MEDIUM: 2.0,
        VehicleSize.LARGE: 3.0
    }

    def calculate_fee(self, parking_ticket: ParkingTicket) -> float:
        duration = parking_ticket.get_exit_timestamp() - parking_ticket.get_entry_timestamp()
        hours = (duration // (1000 * 60 * 60)) + 1
        return hours * self.HOURLY_RATES[parking_ticket.get_vehicle().get_size()]