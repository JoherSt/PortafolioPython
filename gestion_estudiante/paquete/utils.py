def pedir_int(mensaje):
    while True:
        try:
            pedir_edad = int(input(mensaje))
            return pedir_edad
        except ValueError:
            print("Debes Ingresar el tipo de valor correspondiente")

def pedir_string(mensaje):
    while True:
        valor = input(mensaje)
        if valor:
            return valor
        print("No puedes dejar el campo vacio")
            