import random

print("Bienvenido al juego de adivinar el número")

secreto = random.randint(1, 10)
intentos = 0
max_intentos = 5
adivinado = False

while intentos < max_intentos and not adivinado:
    intento = int(input("Ingresa un número entre 1 y 10: "))
    intentos = intentos + 1

    if intento == secreto:
        print("¡Ganaste! Adivinaste el número.")
        adivinado = True
    elif intento > secreto:
        print("El número secreto es menor")
    else:
        print("El número secreto es mayor")

if not adivinado:
    print("Perdiste, se acabaron tus intentos. El número secreto era:", secreto)