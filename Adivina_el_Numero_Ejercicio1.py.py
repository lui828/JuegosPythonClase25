from random import randint
#import random
def adivina_el_numero(): 
    numero_secreto = randint(1, 100)
    intentos = 0
    
    print("Bienvenido al juego de adivina el numero!")
    print("Estoy pensando en un numero entre 1 y 100. ¿Puedes adivinar cual es?")

    while True:
        intento = int(input("introduce tu numero!"))
        intentos += 1
        if intento < numero_secreto:
            print("Demasiado bajo, intenta de nuevo.")
        elif intento > numero_secreto:
            print("Demasiado alto, intenta de nuevo.")
        else:
            print(f"Felicidades! Adivinastes el numero en {intentos} intentos")
            break
adivina_el_numero()