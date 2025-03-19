from turtle import *
from time import *
import sys
import random

class NodoPila:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class EstructuraPila:
    def __init__(self):
        self.tope = None

    def insertar(self, dato):
        if self.tope is None:
            self.tope = NodoPila(dato)
            return
        
        nuevo_nodo = NodoPila(dato)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo

    def quitar(self):
        if self.tope is None:
            return "z"

        temp = self.tope
        self.tope = self.tope.siguiente
        return temp.dato

def generarCadena():
    asignacion = random.randint(1, 10000) 
    cadena = ""
    if asignacion != 0:
        cadena += str(0) * asignacion
        cadena += str(1) * asignacion
    return cadena

def animarAutomata(cadena):
    pila = EstructuraPila()  

    speed(8)
    penup(), setpos(-100, 100), pendown()
    begin_fill()
    for lado in range(4):
        if lado % 2 == 0:
            fillcolor("yellow")
            pencolor("blue")
        else:
            fillcolor("red")
            pencolor("blue")
        forward(100)
        right(90)
    end_fill()
    penup(), setpos(-50, 100), pendown()
    setpos(-50, 150), setpos(-45, 140), setpos(-50, 150), setpos(-55, 140)

    penup(), setpos(-50, 0), pendown()
    setpos(-50, -50), setpos(-45, -40), setpos(-50, -50), setpos(-55, -40)
    hideturtle()
    turtle = Turtle()
    
    cadenaMod = cadena
    cadenaPila = "z"
    resultado = "(q," + cadenaMod + "," + cadenaPila + ")⊦\n"

    turtle.penup(), turtle.setpos(-53, 160), turtle.pendown()
    turtle.write(cadenaMod, False, align="left", font=("Lucida Console", 20))
    if cadenaMod[0:1] == '0':
        turtle.penup(), turtle.setpos(-50, 40), turtle.pendown()
        turtle.write('p', False, align="center", font=("Lucida Console", 20))
    cont = -80
    for letra in cadenaPila:
        turtle.penup(), turtle.setpos(-50, cont), turtle.pendown()
        turtle.write(letra, False, align="center", font=("Lucida Console", 20))
        cont -= 20
    sleep(1)
    
    if cadenaMod[0:1] == '1':
        resultado = "La cadena no es aceptada"
    else:
        turtle.clear()
        valido = 1
        estado = 0
        for i in cadena:
            turtle.clear()
            match estado:
                case 0:
                    if int(i) == 0:
                        pila.insertar("x")
                        cadenaMod = cadenaMod[1:]
                        cadenaPila = "X" + cadenaPila
                        resultado += "(q," + cadenaMod + "," + cadenaPila + ")⊦\n"
                    elif int(i) == 1:
                        estado = 1
                        cadenaMod = cadenaMod[1:]
                        cadenaPila = cadenaPila[1:]
                        if cadenaMod == "":
                            resultado += "(p,e," + cadenaPila + ")⊦\n"
                            cadenaMod = "e"
                        else:
                            resultado += "(p," + cadenaMod + "," + cadenaPila + ")⊦\n"
                        pila.quitar()  
                case 1:
                    if int(i) == 1:
                        dato = pila.quitar()
                        if dato == "z":
                            turtle.penup(), turtle.setpos(-53, 160), turtle.pendown()
                            turtle.write(cadenaMod, False, align="left", font=("Lucida Console", 20))
                            turtle.penup(), turtle.setpos(-50, 40), turtle.pendown()
                            turtle.write('f', False, align="center", font=("Lucida Console", 20))
                            cont = -80
                            for letra in cadenaPila:
                                turtle.penup(), turtle.setpos(-50, cont), turtle.pendown()
                                turtle.write(letra, False, align="center", font=("Lucida Console", 20))
                                cont -= 20
                            sleep(1)
                            break

                        cadenaMod = cadenaMod[1:]
                        cadenaPila = cadenaPila[1:]
                        if cadenaMod == "":
                            resultado += "(p,e," + cadenaPila + ")⊦\n"
                            cadenaMod = "e"
                        else:
                            resultado += "(p," + cadenaMod + "," + cadenaPila + ")⊦\n"
                    else:
                        turtle.penup(), turtle.setpos(-53, 160), turtle.pendown()
                        turtle.write(cadenaMod, False, align="left", font=("Lucida Console", 20))
                        turtle.penup(), turtle.setpos(-50, 40), turtle.pendown()
                        turtle.write('f', False, align="center", font=("Lucida Console", 20))
                        cont = -80
                        for letra in cadenaPila:
                            turtle.penup(), turtle.setpos(-50, cont), turtle.pendown()
                            turtle.write(letra, False, align="center", font=("Lucida Console", 20))
                            cont -= 20
                        sleep(1)
                        break

            turtle.penup(), turtle.setpos(-53, 160), turtle.pendown()
            turtle.write(cadenaMod, False, align="left", font=("Lucida Console", 20))
            turtle.penup(), turtle.setpos(-50, 40), turtle.pendown()

            if cadenaMod[0:1] == '0':
                turtle.write('q', False, align="center", font=("Lucida Console", 20))
            else:
                turtle.write('p', False, align="center", font=("Lucida Console", 20))
            cont = -80
            for letra in cadenaPila:
                turtle.penup(), turtle.setpos(-50, cont), turtle.pendown()
                turtle.write(letra, False, align="center", font=("Lucida Console", 20))
                cont -= 20
            sleep(1)

        turtle.penup(), turtle.setpos(-53, 160), turtle.pendown()          
        
        dato = pila.quitar()
        if dato == "z" or valido == 0:
            resultado += "(f,e,z)"
            turtle.clear()
            turtle.penup(), turtle.setpos(-53, 160), turtle.pendown()
            turtle.write('e', False, align="left", font=("Lucida Console", 20))
            turtle.penup(), turtle.setpos(-50, 40), turtle.pendown()
            turtle.write('f', False, align="center", font=("Lucida Console", 20))
            cont = -80
            for letra in cadenaPila:
                turtle.penup(), turtle.setpos(-50, cont), turtle.pendown()
                turtle.write(letra, False, align="center", font=("Lucida Console", 20))
                cont -= 20
            sleep(1)
            
            turtle.penup(), turtle.setpos(-153, 200), turtle.pendown()
            turtle.write('La cadena es aceptada', False, align="left", font=("Lucida Console", 20))
            
            resultado += "\nLa cadena es aceptada"
        else:
            if cadenaMod == "":
                resultado += "(f,e," + cadenaPila + ")\n"
            else:
                resultado += "(f," + cadenaMod + "," + cadenaPila + ")\n"
            turtle.penup(), turtle.setpos(-153, 200), turtle.pendown()
            turtle.write('La cadena no es aceptada', False, align="left", font=("Lucida Console", 20))
            resultado += "\nLa cadena no es aceptada"
    
    with open("Pila_Automatica_Resultado.txt", "w", encoding="utf-8") as f:
        f.write(resultado)

print("Seleccione una opción:")
print("1. Ingresar la cadena manualmente")
print("2. Generar una cadena automáticamente")

opcion = int(input("Ingrese el número de su opción: "))

if opcion == 1:
    cadena = input("Ingrese la cadena a evaluar (máximo 100,000 caracteres): ")
elif opcion == 2:
    cadena = generarCadena()
    print(f"La cadena generada es: {cadena}")
if len(cadena) <= 100000:
    if len(cadena) <= 10:
        screen = Screen()
        animarAutomata(cadena=cadena)
        screen.mainloop()
    else:
        print("La cadena es demasiado larga para animar el autómata.")
else:
    print("La cadena excede el límite máximo de caracteres (100,000).")