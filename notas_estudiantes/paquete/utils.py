def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Por Favor ingresa un valor válido")


def pedir_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Ingresa un Valor Válido")

def  pedir_string(mensaje):
    while True:
        valor = input(mensaje)

        if valor:
            return valor
        print("No puedes dejar este espacio vacio")

