palabra = input("Escribe una palabra: ")

contador = 0

for letra in palabra.lower():
    if letra == "a":
        contador += 1

print("Cantidad de letras a:", contador)
