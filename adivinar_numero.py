import random

secreto = random.randint(1,100)

while True:
    intento = int(input("Adivina el número: "))

    if intento < secreto:
        print("Muy bajo")
    elif intento > secreto:
        print("Muy alto")
    else:
        print("¡Correcto!")
        break
