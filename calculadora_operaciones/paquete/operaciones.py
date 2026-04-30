from paquete.utils import pedir_int


def suma():
    
    num1 = pedir_int("Ingresa un Numero: ")
    num2 = pedir_int("ingrese un Numero:")
    
    suma = num1 + num2
    print(f"el resultado es: {suma}")

def resta():
    
    num1 = pedir_int("Ingresa un Numero: ")
    num2 = pedir_int("ingrese un Numero:")
    
    resta = num1 - num2
    print(f"El resultado es: {resta}")

def multiplicacion():
    
    num1 = pedir_int("Ingresa un Numero: ")
    num2 = pedir_int("ingrese un Numero:")
    
    multiplicacion = num1 * num2
    print(f"El Resultado es: {multiplicacion}")

def division():
    while True:
        num1 = pedir_int("Ingresa un primer número: ")
        num2 = pedir_int("Ingresa un segundo número: ")

        if num1 == 0:
            print("El segundo número no puede ser cero, intenta de nuevo")
            continue
        elif num2 == 0:
            print("El primer número no puede ser cero, intenta de nuevo")           
            continue

        resultado = num1 / num2
        print(f"El resultado es: {resultado}")
        break


