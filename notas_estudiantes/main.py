from paquete.notas import registrar_estudiantes, mostrar_estudiantes, buscar_estudiante, eliminar_estudiante, editar_notas
from paquete.utils import pedir_string
def mostrar_menu():
    while True:
        print("=" * 30)
        print("=== BIENVENIDO ===")
        print("=" * 30)
        print("1. Registrar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Buscar estudiante")
        print("4. Eliminar estudiante")
        print("5. Editar notas")
        print("6. Salir")

        opcion = pedir_string("Selecciona una opción: ")

        if opcion not in["1", "2", "3", "4", "5", "6"]:
            print("Ingresa un dato valido")
            continue


        if opcion == "1":
            registrar_estudiantes()
        elif opcion == "2":
            mostrar_estudiantes()
        elif opcion == "3":
            buscar_estudiante()
        elif opcion == "4":
            eliminar_estudiante()
        elif opcion == "5":
            editar_notas()
        elif opcion == "6":
            print("Saliendo")
            break
        else:
            print("Opción inválida")


mostrar_menu()

