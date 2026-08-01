while True:

    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Opción: ")

    if opcion == "5":
        break

    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))

    if opcion == "1":
        print(a+b)

    elif opcion == "2":
        print(a-b)

    elif opcion == "3":
        print(a*b)

    elif opcion == "4":
        if b != 0:
            print(a/b)
        else:
            print("No se puede dividir entre cero.")
