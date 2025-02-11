import os
import random
import networkx as nx
import matplotlib.pyplot as plt

actual_jugada = ""
archivo_jugada = ""
archivo_losers = ""
archivo_winners = ""
jugada_final = ""
lis_jugada = []

def main():
    global actual_jugada, archivo_jugada, archivo_losers, archivo_winners, jugada_final, lis_jugada

    # Menú para elegir la forma de entrada
    print("Seleccione el método de entrada para las jugadas:")
    print("1. Generar automáticamente")
    print("2. Ingresar manualmente")
    opcion = input("Ingrese 1 o 2: ")
    
    # Eliminación de archivos existentes
    files_to_remove = [
        "Ajedrez 5x5/jugada_t_1.txt", 
        "Ajedrez 5x5/jugada_g_1.txt", 
        "Ajedrez 5x5/jugada_p_1.txt",
        "Ajedrez 5x5/jugada_t_2.txt", 
        "Ajedrez 5x5/jugada_g_2.txt", 
        "Ajedrez 5x5/jugada_p_2.txt"
    ]
    for file in files_to_remove:
        if os.path.exists(file):
            os.remove(file)
    
    if opcion == '1':
        Inico_Secuenciadad_jugadaimientos = random.randint(5, 100)  # Tamaño automático
        print(f"Tamaño de la cadena: {Inico_Secuenciadad_jugadaimientos}")

        # Configuración de archivos para jugador 1
        archivo_jugada = "Ajedrez 5x5/jugada_t_1.txt"
        archivo_losers = "Ajedrez 5x5/jugada_p_1.txt"
        archivo_winners = "Ajedrez 5x5/jugada_g_1.txt"
        jugada_final = "25,"
        
        # Obtención de jugadas para jugador 1
        obt_play(Inico_Secuenciadad_jugadaimientos, 'r')
        obt_play(actual_jugada, 0, Inico_Secuenciadad_jugadaimientos, 1, "1,")
        save_jug()

        # Limpiar lista y actual jugada
        lis_jugada.clear()
        actual_jugada = ""

        # Configuración de archivos para jugador 2
        obt_play(Inico_Secuenciadad_jugadaimientos, 'b')
        archivo_jugada = "Ajedrez 5x5/jugada_t_2.txt"
        archivo_losers = "Ajedrez 5x5/jugada_p_2.txt"
        archivo_winners = "Ajedrez 5x5/jugada_g_2.txt"
        jugada_final = "21,"
        
        # Obtención de jugadas para jugador 2
        obt_play(actual_jugada, 0, Inico_Secuenciadad_jugadaimientos, 5, "5,")
        save_jug()
        
    elif opcion == '2':
        Inico_Secuenciadad_jugadaimientos = int(input("Ingrese el tamaño de la cadena (entre 5 y 100): "))
        if Inico_Secuenciadad_jugadaimientos < 5 or Inico_Secuenciadad_jugadaimientos > 100:
            print("El tamaño debe estar entre 5 y 100. Saliendo...")
            return

        # Ingresar manualmente la cadena para el jugador 1
        actual_jugada = input("Ingrese la cadena para el jugador 1 (tamaño debe ser igual): ")
        if actual_jugada != actual_jugada[:Inico_Secuenciadad_jugadaimientos]:
            print("La cadena debe ser del mismo tamaño que el especificado. Saliendo...")
            return
        
        archivo_jugada = "Ajedrez 5x5/jugada_t_1.txt"
        archivo_losers = "Ajedrez 5x5/jugada_p_1.txt"
        archivo_winners = "Ajedrez 5x5/jugada_g_1.txt"
        jugada_final = "25,"
        obt_play(actual_jugada, 0, Inico_Secuenciadad_jugadaimientos, 1, "1,")
        save_jug()

        lis_jugada.clear()
        actual_jugada = ""

        # Ingresar manualmente la cadena para el jugador 2
        actual_jugada = input("Ingrese la cadena para el jugador 2 (tamaño debe ser igual): ")
        if actual_jugada != actual_jugada[:Inico_Secuenciadad_jugadaimientos]:
            print("La cadena debe ser del mismo tamaño que el especificado. Saliendo...")
            return

        archivo_jugada = "Ajedrez 5x5/jugada_t_2.txt"
        archivo_losers = "Ajedrez 5x5/jugada_p_2.txt"
        archivo_winners = "Ajedrez 5x5/jugada_g_2.txt"
        jugada_final = "21,"
        obt_play(actual_jugada, 0, Inico_Secuenciadad_jugadaimientos, 5, "5,")
        save_jug()
    else:
        print("Opción no válida. Saliendo...")
        return

def obt_play(Inico_Secuenciadad_jugadaimientos, ultima):
    global actual_jugada
    actual_jugada = "".join(["b" if random.randint(0, 1) == 0 else "r" for _ in range(Inico_Secuenciadad_jugadaimientos - 1)]) + ultima
    print(actual_jugada)

def save_jug():
    global lis_jugada
    try:
        with open(archivo_jugada, "a") as fw1, open(archivo_winners, "a") as fw2, open(archivo_losers, "a") as fw3:
            fw2.write(actual_jugada + "\n")
            for x in lis_jugada:
                if x[-3:] == jugada_final:
                    fw2.write(x + "\n")
                else:
                    fw3.write(x + "\n")
                    fw1.write(x + "\n")
    except Exception as e:
        print(e)

def obt_play(jugada, Inico_Secuencia, Final_Secuencia, state, sec_arm):
    global lis_jugada
    if Inico_Secuencia == Final_Secuencia:
        lis_jugada.append(sec_arm)
    else:
        if actual_jugada[Inico_Secuencia] == 'r':
            if state == 1:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 2, sec_arm + "2,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 5, sec_arm + "6,")
            elif state == 2:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 5, sec_arm + "6,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 8, sec_arm + "8,")
            elif state == 3:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 2, sec_arm + "2,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 4, sec_arm + "4,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 8, sec_arm + "8,")
            elif state == 4:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 3, sec_arm + "3,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 5, sec_arm + "5,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 9, sec_arm + "9,")
            elif state == 5:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 4, sec_arm + "4,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 10, sec_arm + "10,")
            elif state == 6:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 1, sec_arm + "1,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 7, sec_arm + "7,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 11, sec_arm + "11,")
            elif state == 7:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 2, sec_arm + "2,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 6, sec_arm + "6,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 8, sec_arm + "8,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 12, sec_arm + "12,")
            elif state == 8:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 3, sec_arm + "3,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 7, sec_arm + "7,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 9, sec_arm + "9,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 13, sec_arm + "13,")
            elif state == 9:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 4, sec_arm + "4,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 8, sec_arm + "8,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 10, sec_arm + "10,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 14, sec_arm + "14,")
            elif state == 10:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 5, sec_arm + "5,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 9, sec_arm + "9,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 15, sec_arm + "15,")
            elif state == 11:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 6, sec_arm + "6,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 12, sec_arm + "12,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 16, sec_arm + "16,")
            elif state == 12:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 7, sec_arm + "7,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 11, sec_arm + "11,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 13, sec_arm + "13,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 17, sec_arm + "17,")
            elif state == 13:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 8, sec_arm + "8,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 12, sec_arm + "12,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 14, sec_arm + "14,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 18, sec_arm + "18,")
            elif state == 14:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 9, sec_arm + "9,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 13, sec_arm + "13,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 15, sec_arm + "15,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 19, sec_arm + "19,")
            elif state == 15:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 10, sec_arm + "10,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 14, sec_arm + "14,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 20, sec_arm + "20,")
            elif state == 16:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 11, sec_arm + "11,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 17, sec_arm + "17,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 21, sec_arm + "21,")
            elif state == 17:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 12, sec_arm + "12,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 16, sec_arm + "16,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 18, sec_arm + "18,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 22, sec_arm + "22,")
            elif state == 18:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 13, sec_arm + "13,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 17, sec_arm + "17,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 19, sec_arm + "19,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 23, sec_arm + "23,")
            elif state == 19:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 14, sec_arm + "14,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 18, sec_arm + "18,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 20, sec_arm + "20,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 24, sec_arm + "24,")
            elif state == 20:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 15, sec_arm + "15,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 19, sec_arm + "19,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 20, sec_arm + "25,")
            elif state == 21:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 16, sec_arm + "16,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 22, sec_arm + "22,")
            elif state == 22:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 17, sec_arm + "17,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 21, sec_arm + "21,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 23, sec_arm + "23,")
            elif state == 23:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 18, sec_arm + "18,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 22, sec_arm + "22,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 24, sec_arm + "24,")
            elif state == 24:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 19, sec_arm + "19,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 23, sec_arm + "23,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 24, sec_arm + "25,")
            elif state == 25:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 20, sec_arm + "20,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 24, sec_arm + "24,")
        else:
            if state == 1:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 7, sec_arm + "7,")
            elif state == 2:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 1, sec_arm + "1,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 3, sec_arm + "3,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 7, sec_arm + "7,")
            elif state == 3:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 7, sec_arm + "7,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 9, sec_arm + "9,")
            elif state == 4:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 8, sec_arm + "8,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 10, sec_arm + "10,")
            elif state == 5:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 9, sec_arm + "9,")
            elif state == 6:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 2, sec_arm + "2,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 12, sec_arm + "12,")
            elif state == 7:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 1, sec_arm + "1,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 3, sec_arm + "3,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 11, sec_arm + "11,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 13, sec_arm + "13,")
            elif state == 8:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 2, sec_arm + "2,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 4, sec_arm + "4,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 12, sec_arm + "12,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 14, sec_arm + "14,")
            elif state == 9:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 3, sec_arm + "3,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 5, sec_arm + "5,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 13, sec_arm + "13,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 15, sec_arm + "15,")
            elif state == 10:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 4, sec_arm + "4,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 14, sec_arm + "14,")
            elif state == 11:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 7, sec_arm + "7,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 17, sec_arm + "17,")
            elif state == 12:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 6, sec_arm + "6,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 8, sec_arm + "8,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 16, sec_arm + "16,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 18, sec_arm + "18,")
            elif state == 13:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 7, sec_arm + "7,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 9, sec_arm + "9,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 17, sec_arm + "17,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 19, sec_arm + "19,")
            elif state == 14:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 8, sec_arm + "8,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 10, sec_arm + "10,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 18, sec_arm + "18,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 20, sec_arm + "20,")
            elif state == 15:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 9, sec_arm + "9,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 19, sec_arm + "19,")
            elif state == 16:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 12, sec_arm + "12,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 22, sec_arm + "22,")
            elif state == 17:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 11, sec_arm + "11,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 13, sec_arm + "13,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 21, sec_arm + "21,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 23, sec_arm + "23,")
            elif state == 18:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 12, sec_arm + "12,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 14, sec_arm + "14,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 22, sec_arm + "22,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 24, sec_arm + "24,")
            elif state == 19:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 13, sec_arm + "13,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 15, sec_arm + "15,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 23, sec_arm + "23,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 25, sec_arm + "25,")
            elif state == 20:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 14, sec_arm + "14,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 24, sec_arm + "24,")
            elif state == 21:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 17, sec_arm + "17,")
            elif state == 22:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 16, sec_arm + "16,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 18, sec_arm + "18,")
            elif state == 23:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 17, sec_arm + "17,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 19, sec_arm + "19,")
            elif state == 24:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 18, sec_arm + "18,")
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 20, sec_arm + "20,")
            elif state == 25:
                obt_play(jugada, Inico_Secuencia + 1, Final_Secuencia, 19, sec_arm + "19,")

if __name__ == "__main__":
    main()  