import random

def adivinanza_matematica():
    operaciones = ["+", "-", "*", "/"]
    operacion = random.choice(operaciones)
    numero1 = random.randint(1, 10)
    numero2 = random.randint(1, 10)
    
    if operacion == "/":
        numero1 = numero1 * numero2  # Aseguramos que la división sea exacta

    print("¡Bienvenido al juego de Adivinanza Matemática!")
    print(f"Resuelve el siguiente problema: {numero1} {operacion} {numero2}")
    
    # Calculamos la respuesta correcta según la operación
    if operacion == "+":
        respuesta_correcta = numero1 + numero2
    elif operacion == "-":
        respuesta_correcta = numero1 - numero2
    elif operacion == "*":
        respuesta_correcta = numero1 * numero2
    elif operacion == "/":
        respuesta_correcta = numero1 // numero2

    intentos = 3

    while intentos > 0:
        try:
            respuesta = int(input(f"Introduce tu respuesta. Te quedan {intentos} intentos: "))
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue
        
        if respuesta == respuesta_correcta:
            print("¡Correcto! Has resuelto el problema.")
            break
        else:
            intentos -= 1
            if intentos > 0:
                print(f"Incorrecto. Te quedan {intentos} intentos.")
            else:
                print(f"Se acabaron los intentos. La respuesta correcta era {respuesta_correcta}.")

adivinanza_matematica()