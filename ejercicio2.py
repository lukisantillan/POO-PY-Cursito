"""
Crear un sistema para una escuela.

Dos clases principales: 
        -PERSONA
            Atributos:
                -Nombre y edad
            Metodos:
                -Mostrar nombre y edad
        -ESTUDIANTE:
            Hereda de persona
            Atributo Original: 
                -Grado
            Metodo: 
                -Mostrar grado
"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def nombre_y_edad(self):
        print(f"El nombre es {self.nombre} y la edad es : {self.edad}")


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    def mostrar_grado(self):
        print(f"El grado del estudiante es {self.grado}")

luki = Estudiante("Lucas", 20, "Egresado")

pregunta = input("Mostrar datos.. (si-no) ")

if(pregunta.lower() == "si"):
    luki.nombre_y_edad()
    luki.mostrar_grado()