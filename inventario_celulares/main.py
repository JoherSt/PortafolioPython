from paquete.celulares import agregar_celular, mostrar_celular, buscar_marca
from paquete.utils import pedir_string
def menu():
    while True:

        print("==BIENVENIDO==")
        print("1.Ingresar el Celular")
        print("2.Mostrar Celular")
        print("3.Buscar por marca")
        print("4.Salir")

        opcion = pedir_string("Seleccione una opcion: ")

        if opcion  not in["1", "2", "3", "4"]:
            print("Selecciona una de las opciones disponibles")
            continue
        

        if opcion == "1":
            agregar_celular()
        elif opcion == "2":
            mostrar_celular()
        elif opcion == "3":
            buscar_marca()
        elif opcion == "4":
            print("Saliendo del programa")
            break   
        else:
            print("Opcion invalida")



menu()