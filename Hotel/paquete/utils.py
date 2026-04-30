def pedir_int(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Por favor Ingresa el Tipo de Dato Correspondiente")

def pedir_string(mensaje):
    while True:
        valor = input(mensaje)
        if valor:
            return valor
        else:
            print("Por favor Ingresa un valor no vacio")