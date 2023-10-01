"""Class for Car model."""

import math

from clase_python.core.abcs.vehicle_abcs import VehicleABC


MAX_DISTANCE_CAN_TRAVEL = 5

AVAILABLE_CAR_BRANDS = ['Nissan', 'Toyota', 'BMW']

class Car(VehicleABC):

    def __init__(self, brand: str, model: int, door_quantity:int) -> None:
        """Constructor for Car class."""

        self.brand = brand
        self.model = model
        self.door_quantity = door_quantity
        self.distance_traveled = 0
        self.current_location = (0, 0)

    def move(self, additional_distance) -> None:

        if additional_distance <= MAX_DISTANCE_CAN_TRAVEL:
            self.distance_traveled += additional_distance
        else:
            self.distance_traveled = MAX_DISTANCE_CAN_TRAVEL

    def calculate_distance(self, origin, destination):
        return math.dist(origin, destination)  

    def move_towards(self, destination):
        distance_traveled = self.calculate_distance(self.current_location, destination)

        #print(f"Moving {distance_traveled} units towards {destination}")

        self.move(distance_traveled)  
        self.current_location = destination

    

    @property
    def brand(self):
        return self.__brand
    

    @brand.setter
    def brand(self, brand):
        if brand in AVAILABLE_CAR_BRANDS:
            self.__brand = brand
        else:
            print("Ingrese una marca válida")

    @property
    def distance_traveled(self):
        return self.__distance_traveled
    
    
    @distance_traveled.setter
    def distance_traveled(self, distance_traveled):
        self.__distance_traveled = distance_traveled