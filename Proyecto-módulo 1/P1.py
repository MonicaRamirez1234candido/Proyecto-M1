##una lista de tipo tupla con el título y el autor, y el valor será una variable booleana que indica si el libro está disponible o no
libros = {
    ("Título del libro", "Autor del libro"): disponibilidad
}

 ##sistema para almacenar libros
 
 #función para agregar 
def agregar_libro():
    "agregar nuevo libro a la biblioteca"
    print("\n Agregar libro\n")
    #inputs para la interacción del usuario 
    titulo = input("Escribe el titulo del libro")
    autor = input("Agrega el nombre del autor del libro")
    #agrega un nuevo libro al diccionario con el título y el autor como clave, y asigna el valor True para indicar que está disponible en la biblioteca.
    libros[("Título del libro", "Autor del libro")] = True
    
    