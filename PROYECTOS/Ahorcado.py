from random import choice

# Función para elegir la palabra al azar
def palabra_al_azar():
    return choice(["chile","calabaza","vestido","sandalias","responsabilidad","guatemala"])

# Función para convertir la palabra a guiones
def convertir_guiones(palabra_secreta):
    guiones = []
    for n in palabra_secreta:
        guiones.append("_")
    return guiones

# Función para verificar si se ingresa una letra
def verificar():
    letra = ""
    while letra not in "abcdefghijklmnñopqrstuvwxyz" or len(letra) != 1:
        letra = input("Ingresa una letra: ").lower()
    return letra

# Comienzo del juego

palabra_secreta = list(palabra_al_azar())
guiones = convertir_guiones(palabra_secreta)
lista_incorrectas = []
vidas = 7

print("""
BIENVENIDO AL JUEGO DEL AHORCADO
EL JUEGO TRATA DE QUE ADIVINES LAS PALABRAS
PUEDES ESCRIBIR UNA LETRA PARA DARTE UNA PISTA
EL JUEGO TE DIRÁ EN DONDE APARECE LA LETRA
TIENES 7 VIDAS
""")

while True:
    print("\nPalabra:", " ".join(guiones))
    print(f"Vidas: {vidas}")
    intento = verificar()

    # Verificar si la letra ya fue usada
    if intento in lista_incorrectas or intento in guiones:
        print("Ya ingresaste esa letra, intenta otra.")
        continue

    if intento in palabra_secreta:
        for n in range(len(palabra_secreta)):
            if intento == palabra_secreta[n]:
                guiones[n] = intento

        if guiones == palabra_secreta:
            print("\n¡Felicidades, adivinaste la palabra!")
            palabra = "".join(palabra_secreta)
            print(f"La palabra era: {palabra}")
            break
    else:
        lista_incorrectas.append(intento)
        vidas -= 1
        print("\nLetra incorrecta.")
        print("Intentos incorrectos:", lista_incorrectas)

        if vidas == 0:
            print("\nGAME OVER")
            palabra = "".join(palabra_secreta)
            print(f"La palabra era: {palabra}")
            break
