"""
Permite a una clase hija acceder a todos los metodos y tener las propiedades de las clases padres. Por ejemplo si tengo la clase persona y despues estudiante
un estudiante es una persona, por lo tanto puede hacer todo lo de una persona mas lo del estudiante
La herencia nos permite reutilizar codigo, hacinedolo mas eficiente y rapido de manejar.

El padre es la superclase
El hijo la subclase

Herencia jerarquica es cuando todas las clases dependen de un mismo padre
por ejemplo
         --------- Persona ------
         |           |          |
    Empleado   Estudiante   Jefe

Herencia multiple
Cuando un hijo tiene mas de un padre, es decir que hereda cosas de ambos.
"""

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def saludar(self):
        print(f"Hola soy {self.nombre}")

#Herencia Simple
class Empleado(Persona): #Mando como parametro la clase padre, que esta hace que tengamos los mismos atributos que persona, se los debemos pasar como parametros
    def __init__(self, nombre, edad, nacionalidad,trabajo,salario):
        super().__init__(nombre, edad, nacionalidad) #indica lo que quiero heredar de la clase padre, ya que el init agrega los que queramos.
        self.trabajo = trabajo
        self.salario = salario
    def trabajar(self):
        print("Me voy a trabajar.. Nos vemos luego..")

empleado1 = Empleado("Lucas",20,"argentino","Programador", 1000000)