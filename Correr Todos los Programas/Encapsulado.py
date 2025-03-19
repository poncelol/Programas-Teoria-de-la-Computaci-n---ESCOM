import random
import subprocess
import time
import os

programas = ["Ejemplo 1.py", "Ejemplo 2.py", "Ejemplo 3.py", "Ejemplo 4.py"]

ejecutando = True

def ejecutar_programa(nombre_programa):
    if os.path.exists(nombre_programa):
        print(f"Ejecutando {nombre_programa}...")
        try:
            subprocess.run(["python", nombre_programa], check=True)
            print(f"{nombre_programa} finalizado.")
        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar {nombre_programa}: {e}")
    else:
        print(f"{nombre_programa} no encontrado.")

def cerrar_programa():
    global ejecutando
    ejecutando = False
    print("Cerrando programa...")

def ejecutar_programas_aleatoriamente():
    global ejecutando
    try:
        while ejecutando:
            random.shuffle(programas)   
            for programa in programas:
                if not ejecutando:
                    break
                ejecutar_programa(programa)  

                if random.random() < 0.1: 
                    cerrar_programa()
                    break

            if ejecutando:
                time.sleep(5)  

    except KeyboardInterrupt:
        print("Ejecución interrumpida por el usuario.")

def seleccionar_programa_manual():
    print("Selecciona el programa a ejecutar:")
    for idx, programa in enumerate(programas):
        print(f"{idx + 1}. {programa}")

    try:
        eleccion = int(input("Ingresa el número del programa que deseas ejecutar: ")) - 1
        if 0 <= eleccion < len(programas):
            ejecutar_programa(programas[eleccion])
        else:
            print("Selección inválida.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número válido.")

if __name__ == "__main__":
    while True:
        print("Elige una opción:")
        print("1. Ejecutar programas aleatoriamente")
        print("2. Seleccionar y ejecutar un programa manualmente")
        print("3. Salir")

        opcion = input("Ingresa tu opción: ")

        if opcion == "1":
            ejecutar_programas_aleatoriamente()
        elif opcion == "2":
            seleccionar_programa_manual()
        elif opcion == "3":
            cerrar_programa()
            break
        else:
            print("Opción no válida. Por favor, elige 1, 2, o 3.")
