from paquete.jugadores import agregar_jugador, ver_jugador, eliminar_jugador
from paquete.utils import pedir_text

def menu():
    while True:
        print("==BIENVENIDO==")
        print("1.Agregar Jugador: ")
        print("2.Ver Jugador: ")
        print("3.Eliminar Jugador: ")
        print("4.Salir: ")

        opcion = pedir_text("Selecciona Una Opcion: ")

        if opcion not in ["1", "2", "3", "4"]:
            print("Opcion Invalida, Por favor ingresa una opcion valida")
            continue

        if opcion == "1":
            agregar_jugador()
        elif opcion == "2":
            ver_jugador()
        elif opcion == "3":
            eliminar_jugador()
        elif opcion == "4":
            print("Saliendo del Programa")
            break

menu()


