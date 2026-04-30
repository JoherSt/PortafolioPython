from .utils import pedir_int, pedir_correo, pedir_contraseña, pedir_string
from .datos  import cuentas
import getpass


def crear_cuenta():
    print("=== CREAR CUENTA ===")

    nombre = pedir_string("Ingresa tu Nombre: ").strip().title()
    documento = pedir_int("Ingresa tu Documento: ")

    for cuenta in cuentas:
        if cuenta["Documento"] == documento:
            print("Este Documento ya existe ")
            return
    
    contraseña = pedir_contraseña("Ingresa la Contraseña: ")
    edad = pedir_int("Ingresa tu Edad: ")
    telefono = pedir_int("Ingresa tu Teléfono: ")
    correo_electronico = pedir_correo("Ingresa tu Correo Electrónico: ")
    direccion = pedir_string("Ingresa tu Dirección: ").strip()


    cuenta = {
        "Nombre": nombre,
        "Documento": documento,
        "Contraseña": contraseña,
        "Edad": edad,
        "Telefono": telefono,
        "Correo": correo_electronico,
        "Direccion": direccion
    }

    cuentas.append(cuenta)
    print(" Usuario agregado con éxito.")



def iniciar_sesion():
    if not cuentas:
        print("No hay cuentas registradas. Crea una cuenta primero.")
        return None

    print("=== INICIAR SESIÓN ===")

    usuario_ingresado = pedir_string("Ingrese su Nombre: ").strip().title()
    contraseña_ingresada = getpass.getpass("Ingrese la contraseña: ")

    for cuenta in cuentas:
        if cuenta["Nombre"] == usuario_ingresado and cuenta["Contraseña"] == contraseña_ingresada:
            print(" Inicio de sesión exitoso.")
            return cuenta

    print(" Usuario o contraseña incorrectos.")
    return None


def mostrar_cuenta(cuenta):

    print(f"Nombre: {cuenta['Nombre']}")
    print(f"Documento: {cuenta['Documento']}")
    print(f"Edad: {cuenta['Edad']}")
    print(f"Teléfono: {cuenta['Telefono']}")
    print(f"Correo: {cuenta['Correo']}")
    print(f"Dirección: {cuenta['Direccion']}")






