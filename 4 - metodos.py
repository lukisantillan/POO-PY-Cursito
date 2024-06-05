""" 
Los metodos son funciones dentro de las clases, nos sirven para definir las acciones que puede hacer nuestro objet

"""

#Atributos de instancia, nosotros los definimos cuando creamos el objeto. 
class Celular: 
    def __init__(self, marca, modelo, camara): #metodo especial se ejecuta cuando creamos el objeto, es el metodo CONSTRUCTOR. self hace referencia a si mismo, self.modelo == celular.model
        self.marca = marca #Asigna lo que le mandemos por parametro, sin contar el self, que hace referencia a si mismo.
        self.modelo = modelo #Estas lineas definen las propiedades del objeto. 
        self.camara = camara
    def llamar(self):
        print(f"Estas haciendo un llamado.. desde un {self.modelo}") #Le pasamos self como parametro para poder referenciarse a si mismo. 
    def cortar(self):
        print(f"Cortaste la llamada.. desde un {self.modelo}")

celular1 = Celular("Samsung", "S23", "48MP")
celular2 = Celular("Apple", "Iphone 15", "96MP")

celular1.llamar()