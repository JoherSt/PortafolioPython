from paquete.operaciones import suma, resta, multiplicacion, division
from paquete.utils import pedir_text

def menu():
    while True:
        print("__BIENVENIDO__")
        print("1.Suma")
        print("2.Resta")
        print("3.Multiplicacion")   
        print("4.Division")
        print("5.Salir")

        opcion = pedir_text("Selecciona una opcion: ")

        if opcion not in ["1", "2", "3", "4", "5"]:
            print("Ingrese una opcion valida")
            continue


        if opcion == "1":
            suma()
        elif opcion == "2":
            resta()
        elif opcion == "3":
            multiplicacion()
        elif opcion == "4":
            division()
        elif opcion == "5":
            print("Saliendo del Programa")
            break

menu()
