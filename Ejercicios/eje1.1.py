nombre = input("Ingresa tu nombre. ")
edad = int(input("Ingresa tu edad: "))
ingreso_mensual = int(input("Ingresa tus ingresos mesuales: "))

while True:
    if edad >= 18 and ingreso_mensual >= 1000:
        print("Debes Tributar")
    else: 
        print("No debes Tributar")
