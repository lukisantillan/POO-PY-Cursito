"""
LSP : Establece que las clases derivadas deben poder ser sustituibles por sus clases base
Si la clase B es una subclase de A, la clase A deberia poder utilizarse en todos los lugares donde B se utiliza
"""

# class Ave:
#     def volar(self):
#         return "Estoy volando"

# class Pinguino(Ave):
#     def volar(self):
#         return "No puedo volar"

# def hacer_volar(ave = Ave):
#     return ave.volar()

# print(hacer_volar(Pinguino()))
#No cumple con el principio ya que Pinguino al derivarse de ave, deberia poder volar, y en este  caso no lo hace

class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        return "Estoy volando"
    
class AveNoVoladora(Ave):
    pass