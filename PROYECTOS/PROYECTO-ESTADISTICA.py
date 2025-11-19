import statistics as stats
import matplotlib.pyplot as plt
import numpy as np

def leer_datos(nombre_archivo):
#Lee los números desde un archivo (separados por comas o saltos de línea)
    numeros = []
    with open(nombre_archivo, 'r') as f:
        for linea in f:
            linea = linea.strip()
            if linea:
                for n in linea.replace(',', ' ').split():
                    try:
                        numeros.append(float(n))
                    except ValueError:
                        pass
    return numeros

def calcular_estadisticas(datos):
    #Calcula las medidas estadísticas básicas.
    n = len(datos)
    media = stats.mean(datos)
    mediana = stats.median(datos)
    try:
        moda = stats.mode(datos)
    except stats.StatisticsError:
        moda = "No hay una moda única"
    minimo = min(datos)
    maximo = max(datos)
    rango = maximo - minimo
    varianza = stats.variance(datos)
    desviacion = stats.stdev(datos)

    return {
        "N": n,
        "Media": media,
        "Mediana": mediana,
        "Moda": moda,
        "Mínimo": minimo,
        "Máximo": maximo,
        "Rango": rango,
        "Varianza": varianza,
        "Desviación Estándar": desviacion
    }

def crear_rangos(datos, k=None):
    """Crea intervalos para agrupar los datos usando la regla de Sturges."""
    n = len(datos)
    if k is None:
        k = int(1 + 3.322 * np.log10(n))  # Formula de Sturges
    minimo = min(datos)
    maximo = max(datos)
    rango_total = maximo - minimo
    amplitud = rango_total / k

    rangos = []
    limites = []
    inicio = minimo
    for i in range(k):
        fin = inicio + amplitud
        limites.append((inicio, fin))
        rangos.append(sum(inicio <= x < fin for x in datos))
        inicio = fin

    return limites, rangos

def mostrar_histograma(limites, frecuencias):
#Histograma a partir de los rangos creados
    etiquetas = [f"{round(a,2)} - {round(b,2)}" for a,b in limites]
    plt.figure(figsize=(10,6))
    plt.bar(etiquetas, frecuencias, width=0.9, color='skyblue', edgecolor='black')
    plt.xlabel("Rangos")
    plt.ylabel("Frecuencia")
    plt.title("Histograma de Frecuencias")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    archivo = input("Ingrese el nombre del archivo con los datos (ej: datos.txt): ")
    datos = leer_datos(archivo)

    if not datos:
        print("No se encontraron datos válidos en el archivo.")
        return

    est = calcular_estadisticas(datos)

    print("\n--- ESTADÍSTICAS ---")
    for k, v in est.items():
        print(f"{k:20}: {v}")

    limites, rangos = crear_rangos(datos)
    print("\n--- DATOS AGRUPADOS ---")
    for (a,b), f in zip(limites, rangos):
        print(f"{round(a,2)} - {round(b,2)} : {f}")

    mostrar_histograma(limites, rangos)

if __name__ == "__main__":
    main()
#EL ARCHIVO DEBE SER .txt ejemplo del contenido
#12,45,78,96,312,85,29,2,85...

