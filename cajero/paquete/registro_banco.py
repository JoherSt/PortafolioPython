from .utils import pedir_int, pedir_float, pedir_texto
from .datos import cuentas



def registro():
    nombre = pedir_texto("Ingresa tu nombre de Usuario: ").lower().strip()
    contraseña = pedir_texto("Ingresa tu contraseña: ").strip()
    tarjeta = pedir_int("Por favor Ingresa tu tarjeta: ")
    tipo_cuenta = pedir_texto("Ingresa el tipo de cuenta: (Ahorros/Corriente): ").lower()

    

    if tipo_cuenta == "ahorros":
        print("Cuenta de Ahorros Seleccionada")
    elif tipo_cuenta == "corriente":
        print("Cuenta corriente seleccionada: ")


    cuenta = {
        "nombre" : nombre,
        "contraseña" : contraseña,
        "tarjeta" : tarjeta,
        "tipo_cuenta" : tipo_cuenta
    }

    cuentas.append(cuenta)
    print("Cuenta agregada exitosamente")

def iniciar_sesion():
    if not cuentas:
        print("No hay ninguna cuenta agregada")
        return

    nombre = pedir_texto("Ingresa tu nombre: ").lower().strip()
    contraseña = pedir_texto("Ingresa tu contraseña: ").strip()

    for cuenta in cuentas:
        if cuenta["nombre"] == nombre and cuenta["contraseña"] == contraseña:
            print("Inicio de sesion Exitoso")
            return 
    print("Nombre o Contraseña Incorrectos")

def mostrar_cuenta():
    if not cuentas:
        print("No hay cuentas Registradas: ")
        return
    
    nombre = pedir_texto(" Por favor Ingresa el nombre de la Cuenta: ").lower().strip()
    
    encontrada = False
    for cuenta in cuentas:
        if cuenta["nombre"] == nombre:
            print(f"nombre {cuenta['nombre']}")
            print(f"tarjeta {cuenta['tarjeta']}")
            print(f"Tipo de Cuentas {cuenta['tipo_cuenta']}")
            encontrada = True
            break
    
    if not encontrada:
        print("No existe cuenta con este nombre")



def pedir_monto():
    while True:
        print("==SELECCIONA EL MONTO QUE QUIERES RETIRAR==")
        print("1.10.000: ")
        print("2.20.000: ")
        print("3.50.000: ")
        print("4.100.000: ")
        print("5.Otro valor: ")

        opcion = pedir_texto("Selecciona una de las opciones para retirar: ")
        
        if opcion == "1":
            monto = 10000
        elif opcion == "2":
            monto = 20000
        elif opcion == "3":
            monto = 50000
        elif opcion == "4":
            monto = 100000
        elif opcion == "5":
            monto = pedir_float("Ingresa el monto que quieres retirar: ")
        else:
            print("Ingresa un valor valido: ")
            continue
        print(f"Monto Retirado: {monto}")
        return monto
        





             


