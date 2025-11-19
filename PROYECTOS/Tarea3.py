texto= input("Ingresa un texto cualquiera, mayor a 20 palabras: ")
letra1=input("Ingresa una letra: ")
letra2=input("Ingresa una letra: ")
letra3=input("Ingresa una letra: ")


print(f"la letra: {letra1} aparace  {texto.count(letra1) } veces")
print(f"la letra: {letra2} aparace  {texto.count(letra2) } veces")
print(f"la letraa:{letra3} aparace  {texto.count(letra3) } veces")
lista= texto.split()
print(f"las cantidad detexto que aparece es de {len(lista)} palabras ")
lista.reverse()
nuevaL=" ".join(lista)
print(f"Texto al reves: {nuevaL}")

print(f"La primer letra es:  {(texto[0])}  ")
print(f"La ultima letra es:  {(texto[-1])}  ")

diccionario={ True: "si",  False:"no"}
print(f'La palabra "Python"  {diccionario ["python" in texto.lower()]} esta  en el texto' )