"""
Encapsulamiento : Consiste en proteger metodos o atributos de un objeto.

Cuando y para que se usa, nos permite ocultar complejidad interna dentro de la clase y protege los atributos cuando te los pone privados.
Mejora la legibilidad del codigo, mantenimiento, evolución. 

Como se puede acceder a los datos encapsulados?

tenemos que usar Getters que son metodos para acceder y setters  que son metodos para modificar.
"""

class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre #SuperPrivado - dos guiones bajos
        self._edad = edad #Privado - un guion 

    def get_nombre(self): #Esto es un getter
        return self.__nombre
    
    def set_nombre(self, new_nombre): #Esto es un setter
        self.__nombre = new_nombre



lucas = Persona("Lucas", 20)

nombre = lucas.get_nombre()

print(nombre)

"""
Getters y Setters
Metodos para acceder o modificar a las propiedades privadas.

Decoradores: es una funcion que decora a otra, agrega codigo atras o adelante. Toma una funcion como entrada, le agrega una funcion extra y devuelve una nueva funcion
modificada
"""

