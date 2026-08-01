mayores = 0
menores = 0
iguales = 0

cantidad = int(input("¿Cuántos números deseas ingresar? "))

for i in range(cantidad):
    numero = float(input("Número: 5 "))

    if numero > 0:
        mayores += 1
    elif numero < 0:
        menores += 1
    else:
        iguales += 1

print("Mayores que cero:", mayores)
print("Menores que cero:", menores)
print("Iguales a cero:", iguales)
