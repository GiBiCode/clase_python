"""Test for class Car"""


from clase_python.model.car import MAX_DISTANCE_CAN_TRAVEL, Car


class TestCar:
    """Test class for class Model"""
    #Método que define una prueba unitaria.
    def test_move_distance_traveled_modified(self, car):
        
        car.move(4)

        assert car.distance_traveled == 4

        car.move(5)

        assert car.distance_traveled == 9



    #Prueba unitaria que intenta mover el Car más allá de la distancia máxima.
    def test_move_exceeds_max_distance(self, other_car):

        other_car.move(10)

        assert other_car.distance_traveled == MAX_DISTANCE_CAN_TRAVEL
 
    #Prueba que verifica que al pasar 0 como distancia no cambiará distancia_traveled.
    def test_move_with_zero_distance(self, car):

        initial_distance = car.distance_traveled

        car.move(0)

        assert car.distance_traveled == initial_distance
    
    #Prueba para determinar distancia recorrida desde un punto origen a un punto destino.
    def test_move_towards_destination(self,car):
    
        current_location = (0, 0)
        destination_distance = (5, 5)

        initial_distance = car.distance_traveled

        car.move_towards(destination_distance)

        # Verificar actualización de la ubicació actual y el aumento de la distancia recorrida
        #Con los asserts.
        assert car.current_location == destination_distance

        assert car.distance_traveled > initial_distance


    #Prueba unitaria para actualizar la posición de la clase Car cuando el destino está en otra coordenada:
    def test_move_towar_destination_modified(self,car):
        destination_distance = (10, 15) 
        car.move_towards(destination_distance)
    
        assert car.current_location == destination_distance