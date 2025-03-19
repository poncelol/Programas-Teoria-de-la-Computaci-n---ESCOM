import time
from tkinter import *
from tkinter import messagebox as MessageBox
from turtle import *

def tablero(movj1, movj2):
    speed(0)
    penup()
    backward(250)
    right(-90)
    forward(200)
    right(90)
    pendown()
    recuadro = 1
    filaE = 1
    columnaE = 1
    for fila in range(4):
        for columna in range(4):
            begin_fill()
            for cuadrado in range(4):
                forward(100)
                right(90)
            if fila % 2 ==0:
                if recuadro % 2 == 0:
                        fillcolor('gray')
                else:
                        fillcolor('red')
            else:
                if recuadro % 2 == 0:
                        fillcolor('red')
                else:
                        fillcolor('gray')
            end_fill(),penup(),right(90),forward(25),left(90)
            pendown()
            write(recuadro,False,align="left",font=("Arial",18))
            penup(),left(90),forward(25),right(90)
            pendown()
            recuadro += 1;   #paso a contabilizar el siguiente cuadrado
            forward(100)
            columna += 1
            
        fila +=1
        backward(400)
        right(90)
        forward(100)
        left(90)
    speed(1)
    penup(),setpos(-250,250),pendown()
    write("Jugador 1 -",False,align="left",font=("Arial",15))
    penup(),setpos(-140,250),pendown()
    write(movj1,False,align="left",font=("Arial",15))
    penup(),setpos(-250,225),pendown(),color("purple")
    write("Jugador 2 -",False,align="left",font=("Arial",15))
    penup(),setpos(-140,225),pendown()
    write(movj2,False,align="left",font=("Arial",15))


def mover(jj, valor ):
    cooX=[[-200,125],[-100,125],[0,125],[100,125],
            [-200,25],[-100,25],[0,25],[100,25],
            [-200,-75],[-100,-75],[0,-75],[100,-75],
            [-200,-175],[-100,-175],[0,-175],[100,-175]]

    jj.penup()
    jj.clear()
    jj.setpos(cooX[int(valor)-1])
    jj.pendown()
    jj.begin_fill()
    jj.circle(25)
    jj.end_fill()
    time.sleep(1)


def obtenerj(archivo,jugadas):
    contador=0
    mov=""
    with open(archivo) as arch:
        for linea in arch:
            if contador==0:
                mov+=linea
            else:
                jugadas.append(linea.split(','))
                jugadas[contador-1].remove("\n")
            contador=contador+1
    mov=mov.removesuffix("\n")
    return mov

def jugar(jugadas1, jugadas2,m):
    if jugadas1 and jugadas2:
        ganador=1
        turno=1
        estado1=0
        estado2=0
        fila1=0
        fila2=0
        col1=0
        col2=0
        while ganador!=0:
            if turno==1:
                temp=0
                estado1=jugadas1[int(fila1)][int(col1)]
                salto=0
                if estado1==estado2:
                    contador=0
                    for i in jugadas1:
                        temp=i[col1]
                        contador+=1
                        if temp!= estado2:
                            fila1=contador-1
                            salto=0
                            break
                        salto=1
                    estado1=temp
                if salto==0:
                    mover(j1,estado1)
                    col1+=1
                turno=2
                if col1==len(jugadas1[0]):
                    ganador=0
                    MessageBox.showinfo("Felicitaciones!","Ha ganado el jugador 1")
            elif turno==2:
                temp=0
                estado2=jugadas2[int(fila2)][int(col2)]
                salto=0
                if estado2==estado1:
                    contador=0
                    for i in jugadas2:
                        temp=i[col2]
                        contador+=1
                        if temp!= estado1:
                            fila2=contador-1
                            salto=0
                            break
                        salto=1
                    estado2=temp
                if salto==0:
                    mover(j2,estado2)
                    col2+=1
                turno=1
                if col2==len(jugadas2[0]):
                    ganador=0
                    MessageBox.showinfo("Felicitaciones!","Ha ganado el jugador 2")

    elif not jugadas1 and not jugadas2:
        MessageBox.showinfo("Mensaje","No hay jugadas ganadoras para los jugadores")
    elif not jugadas1:
        MessageBox.showinfo("Felicitaciones!","Gana el jugador 2 por default")
    elif not jugadas2:
        MessageBox.showinfo("Felicitaciones!","Gana el jugador 1 por default")

screen = Screen() # create the screen

jugadas1=[]
jugadas2=[]
movj1=obtenerj(archivo="jugadas1G.txt",jugadas=jugadas1)
movj2=obtenerj(archivo="jugadas2G.txt",jugadas=jugadas2)

tablero(movj1=movj1,movj2=movj2)

j1 = Turtle()
j2 = Turtle()
j1.speed(3)
j2.speed(3)
j2.color("purple")

jugar(jugadas1=jugadas1,jugadas2=jugadas2,m=movj1)

screen.mainloop()