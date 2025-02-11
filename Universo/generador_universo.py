import os
import random

# Generador para crear cadenas de longitud n
def generar_cadenas(n):
    if n == 0:
        yield ''
    else:
        for cadena in generar_cadenas(n - 1):
            yield cadena + '0'
            yield cadena + '1'

# Función para contar el número de '1's y '0's en una cadena
def contar_unos(cadena):
    return cadena.count('1'), cadena.count('0')

# Función para generar el archivo de salida con la 'e' al inicio y las cadenas organizadas por longitud
def generar_archivo_salida_organizado(n, nombre_archivo="Universo/OutUniverso.txt"):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write("{\n")
        archivo.write("e\n")  # Añadir 'e' al principio
        for longitud in range(1, n + 1):  # Iterar por las longitudes de cadena desde 1 hasta n
            for cadena in generar_cadenas(longitud):
                unos, ceros = contar_unos(cadena)
                archivo.write(f"{cadena}, {unos}, {ceros}\n")
        archivo.write("}\n")
    print("Generación de cadenas organizada completada.")

# Función para generar el archivo CSV
def generar_csv_organizado(n, nombre_archivo="Universo/plotDataSet.csv"):
    print(f"Generando cadenas organizadas por longitud para n = {n}...")
    generar_archivo_salida_organizado(n)
    
    print("Generando archivo CSV...")
    with open("Universo/OutUniverso.txt", "r") as archivo, open(nombre_archivo, 'w') as csv_file:
        csv_file.write("id,OnesNumber,ZeroesNumber\n")
        # Empezar a procesar línea por línea, sin cargar todo el archivo a la vez
        idx = 0
        for linea in archivo:
            linea = linea.strip()
            if linea == "{" or linea == "}" or linea == "e":  # Saltar estas líneas
                continue
            cadena, unos, ceros = linea.split(", ")
            csv_file.write(f"{idx},{unos},{ceros}\n")
            idx += 1
    print(f"Archivo CSV generado: {nombre_archivo}")

# Función para mostrar el menú y obtener la entrada del usuario
def menu():
    while True:
        print("\nMenu:")
        print("1. Generar cadenas con n aleatorio entre 1-1000")
        print("2. Elegir n manualmente (1-1000)")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            n = random.randint(1, 1000)  # Limitar el rango para evitar problemas de memoria
            print(f"Generando cadenas con n = {n}")
            generar_csv_organizado(n)
        elif opcion == '2':
            n = int(input("Introduce el valor de n (1-1000): "))  
            if 1 <= n <= 1000:
                generar_csv_organizado(n)
            else:
                print("Por favor, ingresa un número entre 1 y 1000.")
        elif opcion == '3':
            print("Cerrando el programa...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Ejecución del programa
if __name__ == "__main__":
    menu()
