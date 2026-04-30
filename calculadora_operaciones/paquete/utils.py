
def pedir_int(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Ingrese un tipo de valor valido")

def pedir_text(mensaje):
    while True:
        valor = input(mensaje)

        if valor:
            return valor
        print("Ingrese un dato valido")

