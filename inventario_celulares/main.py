from paquete.celulares import agregar_celular, mostrar_celular, buscar_marca, editar_celular, eliminar_celular
from paquete.utils import pedir_string

def menu():
    while True:

        print("==BIENVENIDO==")
        print("1.Ingresar el Celular")
        print("2.Mostrar Celular")
        print("3.Buscar por marca")
        print("4.Editar Equipo")
        print("5.Eliminar Equipo")
        print("6.Salir")


        opcion = pedir_string("Seleccione una opcion: ")

        if opcion not in["1", "2", "3", "4", "5", "6"]:
            print("Selecciona una de las opciones disponibles")
            continue
        

        if opcion == "1":
            agregar_celular()
        elif opcion == "2":
            mostrar_celular()
        elif opcion == "3":
            buscar_marca()
        elif opcion == "4":
            editar_celular()
        elif opcion == "5":
            eliminar_celular()
        elif opcion == "6":
            print("Saliendo del programa")
            break   


menu()