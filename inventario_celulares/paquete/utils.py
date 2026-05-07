def pedir_entero(mensaje):
    while True:
        try: 
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Por favor ingresa un valor correcto")

def pedir_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor 
        except ValueError:
            print("Por favor ingresa un valor correspondiente")

def pedir_bool(mensaje):
    while True:
            valor = input(mensaje +"(Si/No): ").strip().lower()
            if valor == "si":
                return True
            elif valor == "no":
                return False
            else:
                print("Por favor ingresa la respusta correcta: ")
                
def pedir_string(mensaje):
    while True:
        valor = input(mensaje)

        if valor:
            return valor
        print("Este campo no puede ir vacio")

        