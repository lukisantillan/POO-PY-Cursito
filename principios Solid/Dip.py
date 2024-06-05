"""
DIP: Establece que los modulos de alto nivel no deben depender de los de bajo nivel, si no que los dos deben depender de las abstracciones
Las abstracciones no deben depender de los detalles, los detalles si de las abstracciones
"""

# class CorrectorOrtografico:
#     def __init__(self):
#         self.diccionario = Diccionario()
        
#     def corregir_texto(self,texto):
#         #usamos diccionario para corregir el texto
#         pass


# class Diccionario:
#     def verificar_palabra(self, palabra):
#         #Logica para verificar palabras
#         pass
    
#Esto viola el principio ya que corrector depende de diccionarios

from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self,palabras):
        #Logica para verificar palabra
        pass
    
class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabras):
        #logica para ver si la palabra esta en el diccionario
        pass

class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador
        
    def corregir_texto(self,texto):
        #usamos el verificador para corregir el texto
        pass 