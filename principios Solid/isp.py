"""
ISP: Ningun cliente debe depender de interfaces que no use. 
"""

from abc import ABC, abstractmethod

# class Trabajador(ABC):
    
#     @abstractmethod
#     def comer(self):
#         pass
    
#     @abstractmethod
#     def trabajar(self):
#         pass
    
#     @abstractmethod
#     def dormir(self):
#         pass
    
# class Humano(Trabajador):
    
#     def comer(self):
#         print("El humano esta comiendo")
    
#     def trabajar(self):
#         print("El humano esta trabajando")
        
#     def dormir(self):
#         print("El humano esta durmiendo")
        
# class Robot(Trabajador):
    
#     def comer(self):
#         pass
    
#     def trabajar(self):
#         print("El Robot esta trabajando")
        
#     def dormir(self):
#         pass
    
#No cumple con el principio ya que en este ejemplo el robot no come ni duerme, pero dependeria igual de esos metodos para solucionar subdividimos la clase trabajador

class Trabajador(ABC):
        
    @abstractmethod
    def trabajar(self):
        pass
    
class Comedor(ABC):
    
    @abstractmethod
    def comer(self):
        pass
    
class Durmiente(ABC):   
    @abstractmethod
    def dormir(self):
        pass
    
class Humano(Trabajador, Comedor, Durmiente):
    
    def comer(self):
        print("El humano esta comiendo")
    
    def trabajar(self):
        print("El humano esta trabajando")
        
    def dormir(self):
        print("El humano esta durmiendo")
        
class Robot(Trabajador):
    
    def trabajar(self):
        print("El Robot esta trabajando")
    