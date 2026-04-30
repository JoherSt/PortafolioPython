

def pedir_int(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Por favor Ingresa el tipo de dato Solicitado")

def pedir_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Por favor Ingresa un valor valido")

def  pedir_texto(mensaje):
    while True:

        valor = input(mensaje)
        
        if valor:
            return valor
        print("Ingresa el dato correspondiente")



