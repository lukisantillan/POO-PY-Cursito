"""
Crear una clase estudiante que tenga:
Atributos : Nombre,edad y grado
Metodos : Estudiar y muestre por pantalla el estudiante {nombre} está estudiando"
crear el objeto
pedirle los atributos al usuairo
"""

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado 
    def estudiando(self):
        print(f"El estudiante {self.nombre} está estudiando..")
    def dejar_de_estudiar(self):
        print(f"El estudiante {self.nombre} dejó de estudiar")

nombre = input("Ingrese el nombre del estudiante.. ")
edad = int(input("Ingrese la edad del estudiante.. "))
grado = input("Ingrese el grado del estudiante.. ")

estudiante1 = Estudiante(nombre,edad,grado)

print(f"""
      DATOS DEL ESTUDIANTE : \n\n
      Nombre:{estudiante1.nombre} \n
      Edad: {estudiante1.edad} \n
      Grado: {estudiante1.grado}
      """)

flag = True
while flag:
    estudiar = input("Queres poner al estutdiante a estudiar..?")
    if (estudiar.lower() == "si"):
        estudiante1.estudiando()
    elif(estudiar.lower() == "no"):
        estudiante1.dejar_de_estudiar()
        flag = False