from paquete.prestamo import agregar_producto, mostrar_producto, buscar_producto, vender_producto, editar_producto
from paquete.utils import pedir_string

def menu():
    while True:
        print("==BIENVENIDO==")
        print("1.Agregar Producto: ")
        print("2.Mostrar Producto: ")
        print("3.Buscar Producto: ")
        print("4.Vender Producto: ")
        print("5.Editar Producto: ")
        print("6.Salir: ")

        opcion = pedir_string("Selecciona una Opcion: ")

        if opcion not in["1", "2", "3", "4", "5", "6"]:
            print("Dato no valido")
            continue

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_producto()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            vender_producto()
        elif opcion == "5":
            editar_producto()
        elif opcion == "6":
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opcion invalida. Por favor intenta de nuevo.")


menu()

    