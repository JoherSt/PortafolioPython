from .datos import books
from .utils import pedir_texto

def agregar_books():
    titulo = pedir_texto("Ingresa el titulo del libro: ").lower()
    autor = pedir_texto("Ingresa el Nombre del autor: ") .lower()

    

    libros = {
        "titulo" : titulo,
        "autor" :  autor
    }

    books.append(libros)
    print("Agregado Correctamente")

def buscar_books():

    
    if not books:
        print("No hay libros")
        return

    mostrar = pedir_texto("Ingresa el nombre de el libro que solicita: ").lower()
    

    for book in books:
        if book['titulo'] == mostrar:
            print(f"Su libro es: {book}")
            return
        
    print("No se encontro un libro con este nombre")

def eliminar_book():

    if not books:
        print("No se encontro ningun libro")
        return
    
    print("Si no desea eliminar nada solo presione ENTER para cancelar")    
    eliminar = input("Por favor ingresa el nombre del libro que quiere eliminar: ").lower()

    if not eliminar:
        print("Eliminacion Cancelada")
        return
    
    for book in books:
        if book['titulo'] == eliminar:
            books.remove(book)
            print("el Libro se elimino correctamente")
            return
    print("No se encontro ningun libro con este nombre")

def edit_book():
    if not books:
        print("No hay Ningun libro agregado")
        return
    
    edit = pedir_texto("Ingresa el titulo que quieres editar: ")

    for book in books:
        if book['titulo'] == edit:
            nuevo_titulo = input(f" nuevo titulo ({book['titulo']}): ")
            nuevo_autor = input(f"Nuevo Autor ({book['autor']}): ")

            if nuevo_titulo:
                book['titulo'] = nuevo_titulo
            if nuevo_autor:
                book['autor'] = nuevo_autor

            print("Libro actualizado correctamente")
            return

    print("No hay Libros con este nombre ")




