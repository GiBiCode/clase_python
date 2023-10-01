"""Configuration test file"""

import pytest

from clase_python.model.car import Car


@pytest.fixture()
def car():
    return Car("BMW", 2020,4)

#Fixture para agregar otra instancia de Car con otros valores.
@pytest.fixture()  
def other_car():
  return Car("Toyota", 2022, 2)

