import threading
import time
import random


def procesar_usuario(user_id, **kwargs):
    time.sleep(random.uniform(0.5, 2.0))
    print(f"Procesando usuario ID: {user_id}, Nombre: {kwargs.get('nombre')}, Edad: {kwargs.get('edad')}")

usuarios = [
    (1, {"nombre": "Alice", "edad": 30}),
    (2, {"nombre": "Bob", "edad": 25}),
    (3, {"nombre": "Charlie", "edad": 35}),
    (4, {"nombre": "Diana", "edad": 28}),
    (5, {"nombre": "Eve", "edad": 22}),
]

hilos = []

for user in usuarios:
    user_id, user_info = user
    hilo = threading.Thread(target=procesar_usuario, args=(user_id,), kwargs=user_info)
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()
print("Todos los hilos han finalizado.")
