def pedir_text(mensaje):
    while True:
        texto = input(mensaje)
        if texto:
            return texto
        print("El campo no puede estar vacio. Por favor, ingresa un valor valido.")
        