from paquete.libros import agregar_books, buscar_books, eliminar_book, edit_book
from paquete.utils import pedir_texto

def menu():
    while True:
        print("==BIENVENIDO==")
        print("1.Agregar Libro: ")
        print("2.Mostrar libro: ")
        print("3.Eliminar Libro: ")
        print("4.Editar Libro: ")
        print("5.Salir: ")
        
       
        opcion = pedir_texto("Selecciona una opcion: ")

        if opcion not in ["1","2","3","4","5"]:
            print("Elije una opcion acorde")
            continue        

        if opcion == "1":
            agregar_books()
        elif opcion == "2":
            buscar_books()
        elif opcion == "3":
            eliminar_book()
        elif opcion == "4":
            edit_book()
        elif opcion == "5":
            print("Saliendo del programa")
            break



menu()