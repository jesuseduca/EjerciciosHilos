import threading

class SesionUsuario:
    def __init__(self):
        self.nombre_usuario = None

    def iniciar_sesion(self, nombre_usuario):
        self.nombre_usuario = nombre_usuario
        print(f"Sesión iniciada para el usuario: {self.nombre_usuario}")

datos_sesion = threading.local()

def gestionar_sesion(nombre_usuario):
    datos_sesion.sesion_usuario = SesionUsuario()
    datos_sesion.sesion_usuario.iniciar_sesion(nombre_usuario)

nombres_usuarios = ["Ana", "Carlos", "Beatriz", "David", "Elena"]


hilos = []


for nombre in nombres_usuarios:
    hilo = threading.Thread(target=gestionar_sesion, args=(nombre,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

