# import sys

# sys.path.append("/home/usuario/curso_python/primer_proyecto/clase_python")


from model.car import Car

def main():

    carro1: Car = Car("Nissan", 2020, 4)

    carro1.move(4)

    print(carro1.distance_traveled)

#Verificar si el script se está ejecutando como el programa principal.
if __name__ == "__main__":
    main()