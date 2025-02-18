##una lista de tipo tupla con el título y el autor, y el valor será una variable booleana que indica si el libro está disponible o no
libros = {
    ("Título del libro", "Autor del libro"): disponibilidad
}

 ##sistema para almacenar libros
 
 #función para agregar:
def agregar_libro():
    "agregar nuevo libro a la biblioteca"
    print("\n Agregar libro\n")
    #inputs para la interacción del usuario 
    titulo = input("Escribe el titulo del libro")
    autor = input("Agrega el nombre del autor del libro")
    #agrega un nuevo libro al diccionario con el título y el autor como clave, y asigna el valor True para indicar que está disponible en la biblioteca.
    libros[("Título del libro", "Autor del libro")] = True
    
       #si el libro está disponible:
    print(f"Libro '{titulo}' de {autor} agregado con éxito.\n")
#función de buscador:
def buscar_libro ():
    print("Buscar Libro...")
    #condicional de opción de busqueda por titulo o autor del libro
    clave = input("¿Buscar por título o autor? (título/autor): ").lowe()#para que el programa detecte las mayusculas y minusculas por igual
    
    #buscar por titulo
    if clave == 'título':
        titulo = input ("introduce el titulo del libro: ")
    resultados = [libro for libro, disponible in libros.items() if libro[0].lower() == titulo.lower()]
    
        #buscar por autor
elif clave == 'autor':
autor = input("Introduce el nombre del autor del libro: ")
resultados = [libro for libro, disponible in libros.items() if libro[1].lower() == autor.lower()]
    #sino es valido ninguno:   
else:
print("no es valido")
        
