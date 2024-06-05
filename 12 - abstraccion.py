"""
Significa manejar la complejidad ocultando todos los detalles innecesarios y dando solo las funcionabilidades relevantes.

Abstraccion como mecanismo: nos permite crear clases abstractas.

una clase abstracta es una plantilla para crear clases a partir de ella. 

implementar un metodo es definir como va a funcionar. 
"""

from abc import ABC, abstractmethod

#clases abstractas
class Persona(ABC):
    @abstractmethod
    def __init__(self,nombre,edad,sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    
    @abstractmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"Hola, me llamo : {self.nombre} y tengo {self.edad} años")


class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")

    

#ABSTRACCION
class Auto():
    def __init__(self):
        self.__estado = "apagado"
    
    def encender(self):
        self.__estado = "encendido"
        print("El auto está encendido")
    
    def conducir(self):
        if self.__estado == "apagado":
            self.encender()
        print("Conduciendo el auto")

    
# auto = Auto()

# auto.conducir() #esto es abstraccion



