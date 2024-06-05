class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def saludar(self):
        print(f"Hola soy {self.nombre}")

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return(f"Mi habilidad es {self.habilidad}")

class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad,habilidad,empresa,salario):
        Persona.__init__(self,nombre,edad,nacionalidad) #HERENCIA MULTIPLE
        Artista.__init__(self,habilidad) #HERENCIA MULTIPLE
        self.salario = salario
        self.empresa = empresa
    def presentarse(self):
        print(f"Hola soy : {self.nombre}, {super().mostrar_habilidad()} y trabajo en {self.empresa}") # Usamos super para indicar que lo estamos heredando desde arriba. no usamos self porque estariamos accediendo al metodo interno
                                                #(reescrito), usando super, indicamos que es el metodo de la clase padre

lucas = EmpleadoArtista("Lucas", 20, "argentino", "Trolear", "El basurero", 10000)
lucas.presentarse()

herencia = issubclass(EmpleadoArtista, Artista) #Devuelve True o false para saber si heredan propiedades 
instancia = isinstance(lucas,EmpleadoArtista) #Devuelve true o false dependiendo si es un objeto de la clase que preguntamos 

"""

Que pasa si hay dos clases que tienen la misma propiedad o atributo, esto lo define el MRO que es la forma en la que pyhton dará prioridad.
"""