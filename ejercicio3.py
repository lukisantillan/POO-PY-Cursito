"""
Crear tres clases:
    -Animal
        metodo: Comer
    -Mamifero
        metodo: amamantar
    -Ave
        metodo: volar
crear clase murcielago que herede de mamifero y ave por lo tanto debe ser capaz de amamantar y volar, ademas de comer

finalmente estudia como cambia el comportamiento del MRO al usar super
"""

class Animal:
    def comer(self):
        print("El animal esta comiendo")

class Mamifero(Animal):
    def amamantar():
        print("El animal esta amamantando")

class Ave(Animal):
    def volar():
        print("El animal esta volando")

class Murcielago(Mamifero, Ave):
    pass
