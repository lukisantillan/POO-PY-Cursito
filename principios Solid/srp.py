#SRP- Responasbilidad unica, una clase tiene que tener una sola razon para cambiar, tiene que tener una sola tarea. Una clase tiene que cumplir una unica funcionabilidad
#La clase debe poder realizar su funcion sin depender de otra clase.
class Auto():
    def __init__(self,tanque):
        self.posicion = 0
        self.tanque = tanque

    def mover(self,distancia):
        if self.tanque.obtener_combustible() >= distancia /2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
        else:
            print("No hay combustible suficiente")
    def obtener_posicion(self):
        return self.posicion
    
    # def agregar_combustible(self,cantidad):
    #     self.combustible += cantidad
        
    # def obtener_combustible(self):
    #     return self.combustible
    #Esto no cumple con el SRP, ya que esta clase se encarga de agregar y sacar combustible ademas de mover el auto

class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100

    def obtener_combustible(self, cantidad):
        self.combustible += cantidad

    def usar_combustible(self,cantidad):
        self.combustible -= cantidad
    
    def obtener_combustible(self):
        return self.combustible
    
tanque = TanqueDeCombustible()
autito = Auto(tanque)