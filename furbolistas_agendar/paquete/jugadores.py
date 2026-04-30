from .datos import jugadores
from .utils import pedir_text

def agregar_jugador():
    futbolista = pedir_text("Ingresa el Nombre del Jugador: ")
    equipo = pedir_text("Ingresa el equipo en el que juega: ")

    jugador = {
        "futbolista" : futbolista,
        "equipo" : equipo 
    }
    
    jugadores.append(jugador)
    print("El Jugador se agrego correctamente")

def ver_jugador():
    if not jugadores:
        print("No hay Ningun Jugador Resgistrado")
        return
    
    ver = pedir_text("Ingresa el nombre del futbolista que quieres ver: ")

    for jugador in jugadores:
        if jugador["futbolista"].lower() == ver.lower():
            print(f"futbolista {jugador['futbolista']}")
            print(f"equipo {jugador['equipo']}")
            return

    print("Jugador no Encontrado")


def eliminar_jugador():
    if not jugadores:
        print("No hay Jugadores Ingresados")
        return 
    
    ver = pedir_text("Ingresa el Nombre del jugador que desea eliminar: ")

    for jugador in jugadores:
        if jugador["futbolista"].lower() == ver.lower():
            jugadores.remove(jugador)
            print("El jugador fue eliminado correctamente")
            return 
        
    print("Jugador no encontrado")




    