contador = 0

while True:

    numero = int(input("Número (0 para terminar): "))

    if numero == 0:
        break

    if numero % 2 != 0:
        contador += 1

print("Cantidad de impares:", contador)
