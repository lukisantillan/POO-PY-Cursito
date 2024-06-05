"""
Crear personajes y que estos se puedan fusionar,

Para ello debemos cambiar el comportamiento del operador + para que cuadno los personajes se fusionen, salga un nuevo personaje con habilidades mejoradas

"""

class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.__nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nuevo_nombre):
        self.nombre = nuevo_nombre

    def __repr__(self):
        return f"{self.nombre} fuerza: {self.fuerza}, Velocidad : {self.velocidad}"
    
    def __add__(self, otro_pj):
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        nueva_fuerza = ((self.fuerza + otro_pj.fuerza)/2) **2
        nueva_velocidad = ((self.velocidad + otro_pj.velocidad)/2) **2
        return Personaje(nuevo_nombre,nueva_fuerza, nueva_velocidad)
    
