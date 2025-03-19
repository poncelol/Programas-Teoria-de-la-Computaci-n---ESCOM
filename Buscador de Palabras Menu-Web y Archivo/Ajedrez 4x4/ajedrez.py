import os
import random

movC1 = ""
nomC = ""
nomP = ""
nomG = ""
fin = ""
jugC1 = []

def main():
    global movC1, nomC, nomP, nomG, fin, jugC1
    
    if os.path.exists("jugadas1C.txt") or os.path.exists("jugadas1G.txt") or os.path.exists("jugadas1P.txt") or \
            os.path.exists("jugadas2C.txt") or os.path.exists("jugadas2G.txt") or os.path.exists("jugadas2P.txt"):
        os.remove("jugadas1C.txt")
        os.remove("jugadas1G.txt")
        os.remove("jugadas1P.txt")
        os.remove("jugadas2C.txt")
        os.remove("jugadas2G.txt")
        os.remove("jugadas2P.txt")
    
    vMov = random.randint(4, 20)
    
    nomC = "jugadas1C.txt"
    nomP = "jugadas1P.txt"
    nomG = "jugadas1G.txt"
    fin = "16,"
    obtenerM(vMov, 'r')
    obtenerJ1(movC1, 0, vMov, 1, "1,")
    guardarC1()
    
    jugC1.clear()
    movC1 = ""
    
    obtenerM(vMov, 'b')
    nomC = "jugadas2C.txt"
    nomP = "jugadas2P.txt"
    nomG = "jugadas2G.txt"
    fin = "13,"
    obtenerJ1(movC1, 0, vMov, 4, "4,")
    guardarC1()

    os.system("python tablero.py")


def obtenerM(vMov, ultima):
    global movC1
    movC1 = "".join(["b" if random.randint(0, 1) == 0 else "r" for _ in range(vMov - 1)]) + ultima
    print(movC1)


def guardarC1():
    global jugC1
    try:
        with open(nomC, "a") as fw1, open(nomG, "a") as fw2, open(nomP, "a") as fw3:
            fw2.write(movC1 + "\n")
            for x in jugC1:
                if x[-3:] == fin:
                    fw2.write(x + "\n")
                else:
                    fw3.write(x + "\n")
                    fw1.write(x + "\n")
    except Exception as e:
        print(e)


def obtenerJ1(mov, cantI, cantS, estado, armado):
    global jugC1
    if cantI == cantS:
        try:
            jugC1.append(armado)
        except Exception as e:
            guardarC1()
    else:
        if movC1[cantI] == 'b':
            if estado == 1:
                obtenerJ1(mov, cantI + 1, cantS, 2, armado + "2,")
                obtenerJ1(mov, cantI + 1, cantS, 5, armado + "5,")
            elif estado == 2:
                obtenerJ1(mov, cantI + 1, cantS, 5, armado + "5,")
                obtenerJ1(mov, cantI + 1, cantS, 7, armado + "7,")
            elif estado == 3:
                obtenerJ1(mov, cantI + 1, cantS, 2, armado + "2,")
                obtenerJ1(mov, cantI + 1, cantS, 4, armado + "4,")
                obtenerJ1(mov, cantI + 1, cantS, 7, armado + "7,")
            elif estado == 4:
                obtenerJ1(mov, cantI + 1, cantS, 7, armado + "7,")
            elif estado == 5:
                obtenerJ1(mov, cantI + 1, cantS, 2, armado + "2,")
                obtenerJ1(mov, cantI + 1, cantS, 10, armado + "10,")
            elif estado == 6:
                obtenerJ1(mov, cantI + 1, cantS, 2, armado + "2,")
                obtenerJ1(mov, cantI + 1, cantS, 5, armado + "5,")
                obtenerJ1(mov, cantI + 1, cantS, 7, armado + "7,")
                obtenerJ1(mov, cantI + 1, cantS, 10, armado + "10,")
            elif estado == 7:
                obtenerJ1(mov, cantI + 1, cantS, 2, armado + "2,")
                obtenerJ1(mov, cantI + 1, cantS, 4, armado + "4,")
                obtenerJ1(mov, cantI + 1, cantS, 10, armado + "10,")
                obtenerJ1(mov, cantI + 1, cantS, 12, armado + "12,")
            elif estado == 8:
                obtenerJ1(mov, cantI + 1, cantS, 4, armado + "4,")
                obtenerJ1(mov, cantI + 1, cantS, 7, armado + "7,")
                obtenerJ1(mov, cantI + 1, cantS, 12, armado + "12,")
            elif estado == 9:
                obtenerJ1(mov, cantI + 1, cantS, 5, armado + "5,")
                obtenerJ1(mov, cantI + 1, cantS, 10, armado + "10,")
                obtenerJ1(mov, cantI + 1, cantS, 13, armado + "13,")
            elif estado == 10:
                obtenerJ1(mov, cantI + 1, cantS, 5, armado + "5,")
                obtenerJ1(mov, cantI + 1, cantS, 7, armado + "7,")
                obtenerJ1(mov, cantI + 1, cantS, 13, armado + "13,")
                obtenerJ1(mov, cantI + 1, cantS, 15, armado + "15,")
            elif estado == 11:
                obtenerJ1(mov, cantI + 1, cantS, 7, armado + "7,")
                obtenerJ1(mov, cantI + 1, cantS, 10, armado + "10,")
                obtenerJ1(mov, cantI + 1, cantS, 12, armado + "12,")
                obtenerJ1(mov, cantI + 1, cantS, 15, armado + "15,")
            elif estado == 12:
                obtenerJ1(mov, cantI + 1, cantS, 7, armado + "7,")
                obtenerJ1(mov, cantI + 1, cantS, 15, armado + "15,")
            elif estado == 13:
                obtenerJ1(mov, cantI + 1, cantS, 10, armado + "10,")
            elif estado == 14:
                obtenerJ1(mov, cantI + 1, cantS, 10, armado + "10,")
                obtenerJ1(mov, cantI + 1, cantS, 13, armado + "13,")
                obtenerJ1(mov, cantI + 1, cantS, 15, armado + "15,")
            elif estado == 15:
                obtenerJ1(mov, cantI + 1, cantS, 10, armado + "10,")
                obtenerJ1(mov, cantI + 1, cantS, 12, armado + "12,")
            elif estado == 16:
                obtenerJ1(mov, cantI + 1, cantS, 12, armado + "12,")
                obtenerJ1(mov, cantI + 1, cantS, 15, armado + "15,")
        else:
            if estado == 1:
                obtenerJ1(mov, cantI + 1, cantS, 6, armado + "6,")
            elif estado == 2:
                obtenerJ1(mov, cantI + 1, cantS, 1, armado + "1,")
                obtenerJ1(mov, cantI + 1, cantS, 3, armado + "3,")
                obtenerJ1(mov, cantI + 1, cantS, 6, armado + "6,")
            elif estado == 3:
                obtenerJ1(mov, cantI + 1, cantS, 6, armado + "6,")
                obtenerJ1(mov, cantI + 1, cantS, 8, armado + "8,")
            elif estado == 4:
                obtenerJ1(mov, cantI + 1, cantS, 3, armado + "3,")
                obtenerJ1(mov, cantI + 1, cantS, 8, armado + "8,")
            elif estado == 5:
                obtenerJ1(mov, cantI + 1, cantS, 1, armado + "1,")
                obtenerJ1(mov, cantI + 1, cantS, 6, armado + "6,")
                obtenerJ1(mov, cantI + 1, cantS, 9, armado + "9,")
            elif estado == 6:
                obtenerJ1(mov, cantI + 1, cantS, 1, armado + "1,")
                obtenerJ1(mov, cantI + 1, cantS, 3, armado + "3,")
                obtenerJ1(mov, cantI + 1, cantS, 9, armado + "9,")
                obtenerJ1(mov, cantI + 1, cantS, 11, armado + "11,")
            elif estado == 7:
                obtenerJ1(mov, cantI + 1, cantS, 3, armado + "3,")
                obtenerJ1(mov, cantI + 1, cantS, 6, armado + "6,")
                obtenerJ1(mov, cantI + 1, cantS, 6, armado + "8,")
                obtenerJ1(mov, cantI + 1, cantS, 11, armado + "11,")
            elif estado == 8:
                obtenerJ1(mov, cantI + 1, cantS, 3, armado + "3,")
                obtenerJ1(mov, cantI + 1, cantS, 11, armado + "11,")
            elif estado == 9:
                obtenerJ1(mov, cantI + 1, cantS, 6, armado + "6,")
                obtenerJ1(mov, cantI + 1, cantS, 14, armado + "14,")
            elif estado == 10:
                obtenerJ1(mov, cantI + 1, cantS, 6, armado + "6,")
                obtenerJ1(mov, cantI + 1, cantS, 9, armado + "9,")
                obtenerJ1(mov, cantI + 1, cantS, 11, armado + "11,")
                obtenerJ1(mov, cantI + 1, cantS, 14, armado + "14,")
            elif estado == 11:
                obtenerJ1(mov, cantI + 1, cantS, 6, armado + "6,")
                obtenerJ1(mov, cantI + 1, cantS, 8, armado + "8,")
                obtenerJ1(mov, cantI + 1, cantS, 14, armado + "14,")
                obtenerJ1(mov, cantI + 1, cantS, 16, armado + "16,")
            elif estado == 12:
                obtenerJ1(mov, cantI + 1, cantS, 8, armado + "8,")
                obtenerJ1(mov, cantI + 1, cantS, 11, armado + "11,")
                obtenerJ1(mov, cantI + 1, cantS, 16, armado + "16,")
            elif estado == 13:
                obtenerJ1(mov, cantI + 1, cantS, 9, armado + "9,")
                obtenerJ1(mov, cantI + 1, cantS, 14, armado + "14,")
            elif estado == 14:
                obtenerJ1(mov, cantI + 1, cantS, 9, armado + "9,")
                obtenerJ1(mov, cantI + 1, cantS, 11, armado + "11,")
            elif estado == 15:
                obtenerJ1(mov, cantI + 1, cantS, 11, armado + "11,")
                obtenerJ1(mov, cantI + 1, cantS, 14, armado + "14,")
                obtenerJ1(mov, cantI + 1, cantS, 16, armado + "16,")
            elif estado == 16:
                obtenerJ1(mov, cantI + 1, cantS, 11, armado + "11,")


if __name__ == "__main__":
    main()
