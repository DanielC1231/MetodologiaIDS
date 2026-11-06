import random

def jugar_cofres():
    print("¡Bienvenido al juego de los cofres misteriosos!")
    print("Hay 5 cofres en total. Encuentra el tesoro antes de gastar tus 3 intentos.")
    
    cofres = [1, 2, 3, 4, 5]
    tesoro = random.choice(cofres)
    
    intentos = 0
    max_intentos = 3
    
    while intentos < max_intentos:
        print("Intentos usados:", intentos, "de", max_intentos)
        
        eleccion = int(input("Elige un cofre (1 al 5): "))
        
        if eleccion == tesoro:
            print("¡Felicidades! Encontraste el tesoro y ganaste el juego.")
            break 
        
        elif eleccion > tesoro:
            print("Te pasaste, el tesoro está en un cofre con un número MENOR.")
        else:
            print("Te quedaste corto, el tesoro está en un cofre con un número MAYOR.")
            
        intentos = intentos + 1
        
    if intentos == max_intentos:
        print("¡Te quedaste sin intentos! Perdiste.")
        print("El tesoro estaba escondido en el cofre número:", tesoro)

jugar_cofres()