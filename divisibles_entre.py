print("Números divisibles entre 3 y 5:")

for numero in range(1, 101):
    if numero % 3 == 0 and numero % 5 == 0:
        print(numero)
