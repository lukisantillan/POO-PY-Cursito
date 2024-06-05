"""
"""

class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre #SuperPrivado - dos guiones bajos
        self._edad = edad #Privado - un guion 

    @property #Le dice al objeto que es un getter, para usarlo como propiedad
    def nombre(self): #Esto es un getter
        return self.__nombre
    
    @nombre.setter #Creamos un decorador para poder modificar y convertir en setter el metodo. 
    def nombre(self, new_nombre): #Esto es un setter
        self.__nombre = new_nombre

    @nombre.deleter #Creamos un decorador para poder eliminar y convertir en deleter el metodo. 
    def nombre(self): #Esto es un deleter
        del self.__nombre   




lucas = Persona("Lucas", 20)

nombre = lucas.nombre

print(nombre)