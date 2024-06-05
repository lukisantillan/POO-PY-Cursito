"""
OCP : Nos dice que las entidades(clases, modulos,funciones), deben estar abiertas para la extension, pero cerradas para la modificacion
significa que deberiamos poder agregarle nuevas funciones, sin cambiar el codigo fuente
"""

class Notificador:
    def __init__(self, ususario,mensaje):
        self.usuario = ususario #se supone que es una clase que almacena email, sms, etc.
        self.mensaje = mensaje
    
    def notificador(self):
        raise NotImplementedError #deja abierto para agregar funcionabilidad, pero no modificar el codigo de notificador
    
class NotificadorEmail(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje por Mail a {self.usuario.email}")
        
class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje por SMS a {self.usuario.sms}")

