from paquete.hotel import crear_cliente, habitaciones_disponibles, reservar_habitacion
from paquete.utils import pedir_string

def menu():
    while True:
        print("==BIENVENIDO==")
        print("1.Ingrese sus datos: ")
        print("2. Habitaciones Disponibles: ")
        print("3. Reservar Habitacion: ")
        print("4. Salir: ")

        opcion = pedir_string("Selecciona una Opcion: ")
        
        if opcion not in["1", "2", "3", "4"]:
            print("Elija una opcion valida")
            continue

        if opcion == "1":
            crear_cliente()
        elif opcion == "2":
            habitaciones_disponibles()
        elif opcion == "3":
            reservar_habitacion()
        elif opcion == "4":
            print("Saliendo del programa")
            break
            

menu()