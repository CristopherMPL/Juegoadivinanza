

from operator import truediv
import random


numero_secreto = random.randint(1,100)
can_intentos = 0
can_max_intentos = 5
adivinado = False

print('bienvenido al juego adivinador')

while not adivinado and can_intentos < can_max_intentos:
    entrada = input('introduce el numero del 1 al 99: ')
    numero = int(entrada)

    if numero == numero_secreto:
        print ("felicitaciones, adivinaste le numero")
        adivinado = True
    elif numero < numero_secreto:
        print("el numero es mayor al ingresado")
    else:
        print('el numero es menor al ingresado')

    can_intentos += 1

if not can_intentos < can_max_intentos: 
    print('¡game over! no adivinaste')