numero = abs(int(input("Ingresa un número: ")))

contador = 0

while numero > 0:
    numero //= 10
    contador += 1

if contador == 0:
    contador = 1

print("Cantidad de dígitos:", contador)
