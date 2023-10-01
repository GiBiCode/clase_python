"""Class for Airplane model."""

from core.abcs.vehicle_abcs import Vehicle


MAX_DISTANCE_CAN_TRAVEL = 5

class Airplane():

    def __init__(self, brand:str, engines_quantity:int, door_quantity:int) -> None:
        """Constructor for Airplane class."""

        self.brand = brand
        self.engines_quantity:engines_quantity
        self.door_quantity = door_quantity
        self.distance_traveled = 0

    def move(self, additional_distance) -> None:

        if additional_distance <= MAX_DISTANCE_CAN_TRAVEL:
            self.distance_traveled += additional_distance

        else:
            self.distance_traveled = MAX_DISTANCE_CAN_TRAVEL