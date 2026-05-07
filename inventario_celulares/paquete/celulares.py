
from .utils import pedir_bool, pedir_entero, pedir_float, pedir_string
from .datos import celulares



def agregar_celular():
    numero_inventario = pedir_entero("Ingresa el numero del inventario: ")
    numero_activo =  pedir_entero("Ingresa el numero del activo: ")
    area = pedir_string("Ingresa el Area: ")
    persona_a_cargo = pedir_string("Ingresa el Nombre de la persona a cargo de este celular: ")
    numero_serie = pedir_entero("Ingresa el numero de serie del celular: ")
    marca = pedir_string(" Ingresa la Marca del Celular: ")   
    modelo = pedir_string("Ingresa El Modelo del Celular: ")
    imei = pedir_string("Ingresa el Imei del Celular: ")
    procesador = pedir_string("Ingresa el procesador del Celular: ")
    ram = pedir_entero("Ingresa la memoria RAM del Celular: ")
    print(f"la memoria ram es {ram} GB")
    almacenamiento = pedir_entero("Ingresa el almacenamiento del Celular: ")
    print(f"El almacenamiento es de {almacenamiento} GB")
    sistema_operativo = pedir_string("Ingrese el sistema operativo del Celular: ")
    tiene_fallas = pedir_bool("El Celular tiene alguna falla:  ")
    estado = pedir_string("En que estado se encuentra el Celular: ")
    valor_costo = pedir_float("Ingresa el precio del Celular: ")
    valor_comercializacion = pedir_float("Ingresa el valor en el que se puede revender este Celular: ")
    diferencia = valor_costo - valor_comercializacion
    print(f"La diferencia del es: {diferencia}")
    color = pedir_string("Ingresa el color del Celular: ")

    
    
    celular = {
    "numero_inventario" : numero_inventario,
    "numero_activo" : numero_activo,
    "area" : area,
    "persona_a_cargo" : persona_a_cargo,
    "numero_serie" : numero_serie,
    "marca" : marca,
    "modelo" : modelo,
    "imei" : imei,
    "procesador" : procesador,
    "ram" : ram,
    "almacenamiento" : almacenamiento,
    "sistema_operativo" : sistema_operativo,
    "Tiene Fallas" : tiene_fallas,
    "estado" : estado,
    "valor_costo" : valor_costo,
    "valor_comercializacion" : valor_comercializacion,
    "diferencia" : diferencia,
    "color" : color
}

    celulares.append(celular)
    print("Equipo agregado correctamente")

def mostrar_celular():
    if not celulares:
        print("no hay equipos registrados")
        return
    
    
    for celular in celulares:
        print(celular)

def buscar_marca():
    if not celulares:
        print("no hay equipos registrados")
        return
    
    buscar_marca = pedir_string("Ingrese la Marca del equipo: ").lower()
    encontrado = False
    

    for celular in celulares:
        if celular["marca"].lower() == buscar_marca:
            print(celular) 
            encontrado = True
    
    if not encontrado:    
        print("No se encontro equipo con esta Marca")

def editar_celular():
    if not  celulares:
        print("No hay equipos Registrados")
        return

    dato = pedir_entero("Ingresa el numero_serie del equipo que quieres editar: ")

    for celular in celulares:
        if celular["numero_serie"] == dato:


            print("Equipo Encontrado")
            for clave, valor in celular.items():
                print(f"{clave}, {valor}")

            print("Escribe el Nuevo valor o presiona ENTER para continuar")

            for clave in celular:
                if clave == "diferencia":
                    continue  

                nuevo_valor = input(f"{clave} ({celular[clave]}): ")

                if nuevo_valor:
                    if clave in ["numero_inventario", "numero_activo", "numero_serie", "ram", "almacenamiento"]:
                       celular[clave] = int(nuevo_valor)
                    elif clave in ["valor_costo", "valor_comercializacion"]:
                        celular[clave] = float(nuevo_valor)
                    elif clave == "Tiene Fallas":
                        celular[clave] = nuevo_valor.strip().lower() == "si"
                    else:
                        celular[clave] = nuevo_valor
            
            celular["diferencia"] = celular["valor_comercializacion"] - celular["valor_costo"]

            print(" Equipo actualizado correctamente.")
            return

    print(" No se encontró un equipo con ese numero.")
                

def eliminar_celular():
    if not celulares: 
        print("No hay equipos registrados.")
        return
        
    print("Si no desea eliminar el equipo presiona ENTER")
    numero = input("Por favor ingresa el activo que deseas eliminar: ")

    if numero == "":    
        print("Operacion Cancelada")
        return

    numero = int(numero)

    encontrado = False
    for celular in celulares:
        if celular["numero_activo"] == numero:
            confirmar = input("¿Confirmar eliminación? (si/no): ")
            if confirmar.lower() == "si":
                celulares.remove(celular)
                print("El equipo se eliminó correctamente.")
            else:
                print("Eliminación cancelada.")
            encontrado = True
            break
    if not encontrado:
        print("No se encontró el equipo.")
            








    




