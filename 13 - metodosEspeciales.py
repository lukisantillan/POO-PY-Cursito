"""
Metodos dunder: 
Son funciones que inician con dos guiones bajos y finalizan de la misma maneras 

sobre carga de operadores: 
"""
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad 

    def __str__(self):
        return f'Persona(nombre={self.nombre}, edad={self.edad})' #nos muestra el objeto en la forma que lo queramos
    
    def __repr__(self):
        return f'Persona(nombre={self.nombre}, edad={self.edad})'
    
    def __add__(self, otro): #definimos como va a actuar el objeto cuando le sumamos cosas
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre, nuevo_valor) 
    


lucas = Persona("Lucas", 21)
repre = repr(lucas)
resultado = eval(repre) #reconstruye el objeto
    