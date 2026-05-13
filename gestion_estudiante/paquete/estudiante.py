from .datos import estudiantes
from .utils import pedir_int, pedir_string

def agregar_estudiante():
    nombre = pedir_string("Ingresa tu Nombre: ").lower()
    edad = pedir_int("Ingresa tu Edad: ")
    curso = pedir_string("Ingresa tu Curso: ")

    estudiante = {
        "nombre" : nombre,
        "edad" : edad,
        "curso" : curso
    }

    estudiantes.append(estudiante)
    print("Estudiante agregado Exitosamente")

def ver_estudiantes():
    if not estudiantes:
        print("No hay Ningun estudiante Registrado")
        return


    for estudiante in estudiantes:
        print(f"{estudiante['nombre']}")
        print(f"{estudiante['edad']}")
        print(f"{estudiante['curso']}")


def buscar_estudiante():
    if not estudiantes:
        print("No hay ningun estudiante Registrado")
        return

    ver = pedir_string("ingresa tu nombre: ").lower()

    for estudiante in estudiantes:
        if estudiante["nombre"] == ver:
            print(f"Nombre: {estudiante['nombre']}")
            print(f"Edad: {estudiante['edad']}")
            print(f"Curso {estudiante['curso']}")
            return

    print("Este usuario no existe: ")    

def eliminar_estudiante():
    if not estudiantes:
        print("No hay estudiantes Registrados: ")
        return
    print("Si No deseas eliminar a ningun estudiante, presiona ENTER:  ")
    eliminar = input("Ingresa el Nombre del estudiante que deseas eliminar: ").lower()

    for estudiante in estudiantes:
        if estudiante['nombre'] == eliminar:
            estudiantes.remove(estudiante)
            print("Estudiante eliminado exitosamente")


