suma = 0
contador = 0

while True:

    numero = float(input("Número: "))

    if numero < 0:
        break

    suma += numero
    contador += 1

if contador > 0:
    print("Media:", suma / contador)
else:
    print("No se ingresaron positivos")
