while True:

    letra = input("Escribe una letra (espacio para terminar): ")

    if letra == " ":
        break

    if letra.lower() in "aeiou":
        print("Vocal")
    else:
        print("Consonante")
