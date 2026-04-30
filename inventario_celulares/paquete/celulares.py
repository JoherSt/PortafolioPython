
from .utils import pedir_bool, pedir_entero, pedir_float, pedir_string
from .datos import celulares



def agregar_celular():
    numero_inventario = pedir_entero("Ingresa el numero del inventario: ")
    numero_activo =  pedir_entero("Ingresa el numero del activo: ")
    area = pedir_string("Ingresa el Area: ")
    persona_a_cargo = pedir_string("Ingresa el Nombre de la persona a cargo de este equipo: ")
    usuario = pedir_string("Ingresa el Usuario: ")
    nombre_equipo = pedir_string("Ingresa el nombre del equipo: ")
    numero_serie = pedir_string("ingresa el numero de serie del equipo: ")
    marca = pedir_string("Por favor Ingresa la Marca: ")   
    modelo_comercial = pedir_string("Ingresa El Modelo: ")
    modelo_fabricante = pedir_string("Ingresa el modelo del fabricante(Opcional)")
    imei = pedir_string("Ingresa el Imei del Equipo: ")
    procesador = pedir_string("Ingresa el procesador del equipo: ")
    ram = pedir_entero("Ingresa la memoria RAM: ")
    print(f"la memoria ram es {ram} GB")
    almacenamiento = pedir_entero("Ingresa el almacenamiento del equipo: ")
    print(f"El almacenamiento es de {almacenamiento} GB")
    sistema_operativo = pedir_string("Ingrese el sistema operativo del Equipo: ")
    tiene_fallas = pedir_bool("El Equipo tiene alguna falla:  ")
    estado = pedir_string("En que estado se encuentra el equipo: ")
    valor_costo = pedir_float("Ingresa el precio del equipo: ")
    valor_comercializacion = pedir_float("ingresa el valor en el que se puede revender este equipo: ")
    diferencia = valor_costo - valor_comercializacion
    print(f"La diferencia del es: {diferencia}")
    color = pedir_string("Ingresa el color del equipo: ")

    
    
    celular = {
    "numero_inventario" : numero_inventario,
    "numero_activo" : numero_activo,
    "area" : area,
    "persona_a_cargo" : persona_a_cargo,
    "usuario" : usuario,
    "nombre_equipo" : nombre_equipo,
    "numero_serie" : numero_serie,
    "marca" : marca,
    "modelo_comercial" : modelo_comercial,
    "modelo_fabricante" : modelo_fabricante,
    "imei" : imei,
    "procesador" : procesador,
    "ram" : ram,
    "almacenamiento" : almacenamiento,
    "sistema_operativo" : sistema_operativo,
    "tiene_fallas" : tiene_fallas,
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
    

    for celular in celulares:
        if celular["marca"].lower() == buscar_marca:
            print(celular) 

    print("No se encontro equipo con esta Marca")







    




