from paquete.inicio_sesion import crear_cuenta, iniciar_sesion, mostrar_cuenta
from paquete.utils import pedir_string

def menu_principal():
    cuenta_actual = None

    while True:
        print("=== BIENVENIDO ===")
        print("1. Crear Cuenta")
        print("2. Iniciar Sesión")
        print("3. Menú Usuario")
        print("4. Salir")

        opcion = pedir_string("Selecciona una opción: ")

        if opcion not in["1", "2", "3", "4"]:
            print("Ingresa una opcion valida")
            continue

        if opcion == "1":
            crear_cuenta()
        elif opcion == "2":
            cuenta_actual = iniciar_sesion()  
        elif opcion == "3":
            if cuenta_actual is None:
                print("Primero debes iniciar sesión")
            else:
                mostrar_cuenta(cuenta_actual)  
        elif opcion == "4":
            print("Saliendo del programa...")
            break

menu_principal()