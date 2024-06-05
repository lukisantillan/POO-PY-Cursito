"""

Se implementa de distintas maneras, hay diferentes tipos.
Polimorfismo es un concepto que hace referencia a poder enivar un mensaje sintactico a diferentes objetos, cuyo mensaje es el mismo, pero el resultado no, gracias
a las propiedades del objeto. Por ejemplo : 
                                        Tenemos un perro,gato y vaca... y les decimos que hagan su ruido, cada uno hara su sonido particular.

Polimorfismo en tiempo de ejecucion es como funciona el lenguaje python. Ya que las variables pueden tener cualquier valor. 

Polimorfismo de sobre carga : permite crear una clase que tenga un mismo metodo pero que su funcionabilidad depende de los parametros que le envies.

Polimorfismo de cohersion: LLego a un resultado sin importar los datos que envio.

Estudiar Duck Typing
Enlaces dinamicos
Enlaces estaticos
tipo real : Es el tipo de donde viene lo que declaramos
tipo declarado : es el tipo que declaramos la variable

"""

class Gato():
    def sonido(self):
        return "Miau"


def hacer_sonido(animal): #Polimorfismo de función
    print(animal.sonido())


class Perro():
    def sonido(self):
        return "Guauf"


perro = Perro()

print(perro.sonido()) 

#Polimorfismo de herencia 

class Animal():
    def sonido(self):
        pass
    
class Ave(Animal):
        pass

class Canguro(Animal):
         pass