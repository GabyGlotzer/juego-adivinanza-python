

import random

numero_secreto = random.randint(0,100)
intentos = 0
max_intentos = 5
adivinado = False

print("bienvenido al juego")

while not adivinado:
    if not intentos < max_intentos:
        print("game over por superar máximo de intentos") 
        break

    entrada = input("Ingresar número del 1 al 99: ") # es string. Convertir a número.
    numero = int(entrada)

    if numero == numero_secreto:
        print("Adivinaste!!!!!")
        adivinado = True
    elif numero < numero_secreto:
        print("el número es mayor al ingresado")
    else:
        print("el número es menor al ingresado")
    
    intentos +=1

