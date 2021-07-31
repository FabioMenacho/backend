# importo no toda la libreria random sino solamente choice para que no pese, ver documentación de pyhton
# random viene instalada en python 
from random import choice


# JUEGO DE PIEDRA PAPEL O TIJERA

# Definir variables de entrada y salida
opciones = ("piedra", "papel", "tijera")
jugador = input("ingresa tu jugada: ")
computadora = choice(opciones)
print("La computadora eligió: " + computadora)
ganador = ""

# Lógica de la solución
if jugador == "piedra":
    if computadora == "piedra":
        ganador = "empate"
    elif computadora =="papel":
        ganador = "computadora"
    elif computadora == "tijera":
        ganador = "jugador"
elif jugador == "papel":
    if computadora == "piedra":
        ganador = "jugador"
    elif computadora =="papel":
        ganador = "empate"
    elif computadora == "tijera":
        ganador = "computadora"
elif jugador == "tijera":
    if computadora == "piedra":
        ganador = "computadora"
    elif computadora =="papel":
        ganador = "jugador"
    elif computadora == "tijera":
        ganador = "empate"

# Muestro el resultado
print ("El ganador es: " + ganador)
