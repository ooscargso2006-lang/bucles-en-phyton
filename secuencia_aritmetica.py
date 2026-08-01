inicio = int(input("Inicio: "))
diferencia = int(input("Diferencia: "))
cantidad = int(input("Cantidad de términos: "))

contador = 0
actual = inicio

while True:

    print(actual)

    actual += diferencia

    contador += 1

    if contador == cantidad:
        break
