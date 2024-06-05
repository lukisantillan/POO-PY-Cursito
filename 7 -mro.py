"""
El metodo de resolucion de orden, es el orden en el que pyhton busca metodos y atributos en las clases. 
Aca super entra en juego.

Depende de el orden en que le pase las herencias en los parametros:
por ejemplo 

D > |B| > C > |A|(VIENE A A, PORQUE B HEREDA DE A). 

"""

class A:
    def hablar(self):
        print("Hola desde A")

class B(A):
    def hablar(self):
        print("Hola desde B")

class C(A):
    def hablar(self):
        print("Hola desde C")

class D(B,C): 
    def hablar(self):
        print("Hola desde B")

d = D()

B.hablar(d) #paso el objeto como parametro para que lo tome como self, en este caso estaria usando el metodo de la clase B, em el objeto d.
D.mro(); #Para saber el orden 