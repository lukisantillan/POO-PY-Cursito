"""
Decoradores: es una funcion que decora a otra, agrega codigo atras o adelante. Toma una funcion como entrada, le agrega una funcion extra y devuelve una nueva funcion
modificada
"""

def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la funcion")
        funcion()
        print("Despues de función")
    return funcion_modificada

# def saludo():
#     print("Hola")

# saludo_modificado = decorador(saludo)
# saludo_modificado()

@decorador #Lo ponemos arriba para indicar que estamos usando un decorador, para no tener que andar asignado. 
def saludo():
    print("Hola")

saludo()