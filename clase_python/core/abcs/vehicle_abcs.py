"""ABCS for Car Class"""

from abc import ABCMeta
from abc import abstractmethod


class VehicleABC(metaclass=ABCMeta):

    @abstractmethod
    def move(self, distance_traveled:int) -> None:
        pass