
x = int(input("Escribe un número: "))
b = 3
c = 5
d = 2

def multiplicar_numeros(x, b):
    resultado = x * b
    return resultado


def sumar_numeros(resultado, c):
    result = resultado + c
    return result  


def dividir_numeros(result, d):
    return result / d  


resultado_multiplicacion = multiplicar_numeros(x, b) 
resultado_suma = sumar_numeros(resultado_multiplicacion, c)  
resultado_division = dividir_numeros(resultado_suma, d)  


print("El resultado final de las operaciones es:", resultado_division)


