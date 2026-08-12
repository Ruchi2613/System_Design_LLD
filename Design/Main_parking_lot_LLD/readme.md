2. How Are the Files Interlinked?
Example Flow:
Vehicle (vehicle.py)

Base class for all vehicles.
Used by ParkingSpot and ParkingFloor to check if a spot fits a vehicle.
VehicleSize (vehicle_size.py)

Enum used by ParkingSpot to define what size it can fit.
Used by ParkingFloor to count available spots by size.
ParkingSpot (parking_spot.py)

Has a size (VehicleSize).
Can check if it’s occupied and if a vehicle can fit.
Used by ParkingFloor.
ParkingFloor (parking_floor.py)

Contains multiple ParkingSpot objects.
Can find an available spot for a vehicle.
Used by ParkingLot.
ParkingLot (parking_lot.py)

Contains multiple ParkingFloor objects.
Handles parking/unparking vehicles.
Used by the demo file.
FeeStrategy (fee_strategy.py)

Used by ParkingLot to calculate fees when a vehicle leaves.
Demo File (parking_lot_demo.py)

Imports all classes.
Creates objects and simulates parking/unparking.


--------------------------------------------------------------------------------------------------------
File/Class	        Imports/Uses	                                Purpose
--------------------------------------------------------------------------------------------------------
ParkingLot	        ParkingFloor, FeeStrategy	                    Manages floors, tickets, fees
ParkingFloor	    ParkingSpot	                                    Manages spots on a floor
ParkingSpot     	Vehicle, VehicleSize	                        Manages a single spot and its vehicle
FeeStrategy	        Used by ParkingLot	                            Calculates parking fees
Demo File	        All above	                                    Runs the whole system


Summary Table
Order	             File/Class	                    Why?
1	                vehicle_size.py	                Used everywhere, no dependencies
2	                vehicle.py	                    Needs VehicleSize
3	                parking_spot.py	                Needs Vehicle, VehicleSize
4	                parking_floor.py	            Needs ParkingSpot
5	                parking_lot.py	                Needs ParkingFloor
6	                fee_strategy.py	                Used by ParkingLot
7	                parking_ticket.py	            Used by ParkingLot
8	                parking_lot_demo.py	            Uses everything
