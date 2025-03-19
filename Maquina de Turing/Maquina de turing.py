from turtle import *
from time import *

class Nodo:
    def __init__(self, dato, nodo):
        self.dato = dato
        self.derecha = None
        self.izquierda = nodo

class Lista:
    def __init__(self):
        self.principal = None

    def insertar(self, dato):
        if self.principal == None:
            self.principal = Nodo(dato, None)
            return

        flecDib = self.principal

        while flecDib.derecha != None:
            flecDib = flecDib.derecha

        nuevo_nodo = Nodo(dato, None)
        nuevo_nodo.izquierda = flecDib
        flecDib.derecha = nuevo_nodo

def maquinaTuring(cadena, max_longitud=1000):
    if len(cadena) > max_longitud:
        print(f"Error: La longitud de la cadena excede el máximo permitido ({max_longitud}).")
        return

    lista = Lista()
    for letra in cadena:
        lista.insertar(letra)

    flecDib = lista.principal
    id = ""

    penup(), setpos(-300, 100), pendown()
    for i in range(len(cadena) + 1):
        for j in range(4):
            forward(50)
            right(90)
        forward(50)
    
    tabla_transiciones = [["Estado", "q0", "q1", "q2", "q3", "q4"],
                         ["0", "(q1,X,R)", "(q1,0,R)", "(q2,0,L)", "-", "-"],
                         ["1", "-", "(q2,Y,L)", "-", "-", "-"],
                         ["X", "-", "-", "(q0,X,R)", "-", "-"],
                         ["Y", "(q3,Y,R)", "(q1,Y,R)", "(q2,Y,L)", "(q3,Y,R)", "-"],
                         ["B", "-", "-", "-", "(q4,B,R)", "-"]]
    
    posx3 = -300
    posy3 = -100
    for i in range(6):
        for j in range(6):
            penup(), setpos(posx3, posy3)
            posx3 += 80
            write(tabla_transiciones[j][i], True, align="center", font=("Lucida Console", 10))
        posy3 -= 20
        posx3 = -300

    tr = Turtle()
    estado = 0
    ultimo = None
    while estado != 4:
        if flecDib == None:
            ultimo.derecha = Nodo("B", nodo=ultimo)
            flecDib = ultimo.derecha
        temp = flecDib

        idt1 = "q" + str(estado) + "_"
        idt2 = ""
        idtsin = ""
        idsin = ""

        while temp != None:
            if temp != None:
                idt1 += temp.dato
                idtsin += temp.dato
            temp = temp.derecha
        temp = flecDib.izquierda
        while temp != None:
            if temp != None:
                idt2 += temp.dato
            temp = temp.izquierda

        id += idt2[::-1] + idt1 + "⊦\n"
        idsin = idt2[::-1] + idtsin

        tr.clear()
        posx = -280
        for i in idsin:
            tr.penup(), tr.setpos(posx, 67), tr.pendown()
            tr.write(i, False, align="left", font=("Lucida Console", 10))
            posx += 50
        posx2 = -280 + (50 * len(idt2))
        tr.penup(), tr.setpos(posx2, 167)
        tr.write("q" + str(estado), False, align="left", font=("Lucida Console", 10))
        tr.penup(), tr.setpos(posx2, 160), tr.pendown()
        tr.setpos(posx2, 110), tr.setpos(posx2 - 5, 115), tr.setpos(posx2, 110), tr.setpos(posx2 + 5, 115)
        tr.penup(), tr.setpos(posx2, -10)
        sleep(1)

        match estado:
            case 0:
                if(flecDib.dato == '0'):
                    estado = 1
                    flecDib.dato = "X"
                    if flecDib.derecha == None:
                        ultimo = flecDib
                    flecDib = flecDib.derecha
                elif(flecDib.dato == 'Y'):
                    estado = 3
                    flecDib.dato = "Y"
                    if flecDib.derecha == None:
                        ultimo = flecDib
                    flecDib = flecDib.derecha
                else:
                    break
            case 1:
                if(flecDib.dato == '0'):
                    estado = 1
                    flecDib.dato = "0"
                    if flecDib.derecha == None:
                        ultimo = flecDib
                    flecDib = flecDib.derecha
                elif(flecDib.dato == '1'):
                    estado = 2
                    flecDib.dato = "Y"
                    if flecDib.derecha == None:
                        ultimo = flecDib
                    flecDib = flecDib.izquierda
                elif(flecDib.dato == 'Y'):
                    estado = 1
                    flecDib.dato = "Y"
                    if flecDib.derecha == None:
                        ultimo = flecDib
                    flecDib = flecDib.derecha
                else:
                    break
            case 2:
                if(flecDib.dato == '0'):
                    estado = 2
                    flecDib.dato = "0"
                    if flecDib.derecha == None:
                        ultimo = flecDib
                    flecDib = flecDib.izquierda
                elif(flecDib.dato == 'X'):
                    estado = 0
                    flecDib.dato = "X"
                    if flecDib.derecha == None:
                        ultimo = flecDib
                    flecDib = flecDib.derecha
                elif(flecDib.dato == 'Y'):
                    estado = 2
                    flecDib.dato = "Y"
                    if flecDib.derecha == None:
                        ultimo = flecDib
                    flecDib = flecDib.izquierda
                else:
                    break
            case 3:
                if(flecDib.dato == 'Y'):
                    estado = 3
                    flecDib.dato = "Y"
                    if flecDib.derecha == None:
                        ultimo = flecDib
                    flecDib = flecDib.derecha
                elif(flecDib.dato == 'B'):
                    estado = 4
                    flecDib.dato = "B"
                    if flecDib.derecha == None:
                        ultimo = flecDib
                    flecDib = flecDib.derecha
                else:
                    break

    if estado == 4:
        id += "\n La cadena es aceptada"
        print("La cadena es aceptada")
        tr.clear()
        posx = -280
        for i in idsin:
            tr.penup(), tr.setpos(posx, 67), tr.pendown()
            tr.write(i, False, align="left", font=("Lucida Console", 10))
            posx += 50
        posx2 = -280 + (50 * len(idt2))
        tr.penup(), tr.setpos(posx2, 167)
        tr.write("q" + str(estado), False, align="left", font=("Lucida Console", 10))
        tr.penup(), tr.setpos(posx2, 160), tr.pendown()
        tr.setpos(posx2, 110), tr.setpos(posx2 - 5, 115), tr.setpos(posx2, 110), tr.setpos(posx2 + 5, 115)
        tr.penup(), tr.setpos(posx2, -10)
        sleep(0)
        tr.penup(), tr.setpos(-250, 200), tr.pendown()
        tr.write("La cadena es aceptada", False, align="left", font=("Lucida Console", 10))
    else:
        id += "\n La cadena no es aceptada"
        print("La cadena no es aceptada")
        tr.penup(), tr.setpos(-250, 200), tr.pendown()
        tr.write("La cadena no es aceptada", False, align="left", font=("Lucida Console", 10))

    print(id)
    with open("IDS.txt", "w", encoding="utf-8") as f:
        f.write(id)
        f.close()

cadena = input("Ingrese la cadena a evaluar: ")
maquinaTuring(cadena=cadena, max_longitud=1000)

screen = Screen()
screen.mainloop()
