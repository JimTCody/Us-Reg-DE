import random
import time

class Usuario():
    Nombre="Carlos"
    Edad=24

    def Registro(self):
        Usuario.Verificar()

    def Verificar():
        print("Verificando informacion")
        time.sleep(1)
        print("Informacion verificada")
        time.sleep(1)
        estadoSig=random.choice(['Denegar', 'Registrar'])

        if estadoSig=='Denegar':
            Usuario.Denegar()
        elif estadoSig=='Registrar':
            Usuario.Registrar()

    def Denegar():
        print("El usuario "+ Usuario.Nombre +" no pudo ser registrado")

    def Registrar():
        print("El usuario "+ Usuario.Nombre +" se registro correctamente")

Usuario.Registro(Usuario)