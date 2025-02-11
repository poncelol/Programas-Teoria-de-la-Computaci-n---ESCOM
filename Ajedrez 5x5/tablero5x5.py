import time
from tkinter import *
from tkinter import messagebox as MessageBox
from turtle import Turtle, Screen

def dibujar_tablero(tortuga):
    tortuga.speed(0)
    tortuga.penup()
    tortuga.setpos(-250, 250)  # Ajustar posición inicial
    tortuga.pendown()
    casilla = 1

    for fila in range(5):
        for columna in range(5):
            tortuga.pencolor('gold')  # Color dorado para el borde
            tortuga.fillcolor('black' if (fila + columna) % 2 != 0 else 'white')
            tortuga.begin_fill()

            # Dibujar cada casilla
            for _ in range(4):
                tortuga.forward(100)
                tortuga.right(90)
            tortuga.end_fill()

            tortuga.penup()
            # Ajustar la posición del número
            tortuga.forward(10)  # Ajuste horizontal
            tortuga.right(90)
            tortuga.forward(25)
            tortuga.left(90)
            
            # Escribir el número en dorado
            tortuga.pencolor('gold')
            tortuga.write(casilla, False, align="left", font=("Arial", 18, "bold"))
            casilla += 1
            
            # Regresar a la posición del cuadrado
            tortuga.left(90)
            tortuga.forward(25)
            tortuga.right(90)
            tortuga.backward(10)  # Volver al inicio
            
            tortuga.pendown()
            # Moverse a la siguiente casilla
            tortuga.forward(100)

        # Ir a la siguiente fila
        tortuga.penup()
        tortuga.backward(500)  # Regresar al inicio de la fila
        tortuga.right(90)
        tortuga.forward(100)
        tortuga.left(90)
        tortuga.pendown()

    tortuga.penup()
    tortuga.setpos(-250, 250)  # Reposicionar para el siguiente elemento
    tortuga.pendown()

def desplazar_ficha(tortuga, valor, color_ficha):
    if valor == '' or not valor.isdigit():  # Validación adicional
        print(f"Valor inválido: '{valor}'")
        return

    # Coordenadas de las posiciones en el tablero
    coordenadas = [[-200 + (100 * (i % 5)), 200 - (100 * (i // 5))] for i in range(25)]

    # Configurar la posición inicial de la ficha
    tortuga.penup()
    tortuga.clear()
    
    # Animar el movimiento hacia la nueva posición
    for paso in range(10):  # Número de pasos de la animación
        x = coordenadas[int(valor) - 1][0] * (paso + 1) / 10
        y = coordenadas[int(valor) - 1][1] * (paso + 1) / 10
        tortuga.setpos(x, y)
        time.sleep(0.05)  # Controlar la velocidad de la animación
    
    # Dibujar la ficha en la posición final
    tortuga.setpos(coordenadas[int(valor) - 1])  # Ir a la posición final
    tortuga.pendown()
    tortuga.color(color_ficha)  # Cambiar el color de la ficha
    tortuga.begin_fill()
    tortuga.circle(25)  # Tamaño de la ficha
    tortuga.end_fill()
    time.sleep(1)

def cargar_jugadas(archivo, jugadas):
    movimientos = ""
    with open(archivo) as arch:
        for contador, linea in enumerate(arch):
            if contador == 0:
                movimientos += linea.strip()  # Eliminar espacios y saltos de línea
            else:
                jugada = linea.strip().split(',')  # Eliminar espacios y saltos de línea
                jugada = [j.strip() for j in jugada if j.strip()]  # Limpiar entradas vacías
                if jugada:  # Solo añadir si no está vacío
                    jugadas.append(jugada)
    return movimientos

def reiniciar_juego():
    global jugadas1, jugadas2
    jugadas1.clear()
    jugadas2.clear()
    movj1 = cargar_jugadas(archivo="Ajedrez 5x5/jugada_g_1.txt", jugadas=jugadas1)
    movj2 = cargar_jugadas(archivo="Ajedrez 5x5/jugada_t_2.txt", jugadas=jugadas2)

    tortuga_tablero.clear()
    dibujar_tablero(tortuga_tablero)

    j1.clear()
    j2.clear()
    iniciar_juego(jugadas1=jugadas1, jugadas2=jugadas2, movimientos=movj1)

def iniciar_juego(jugadas1, jugadas2, movimientos):
    if jugadas1 and jugadas2:
        ganador = 1
        turno = 1
        estado1 = 0
        estado2 = 0
        fila1 = 0
        fila2 = 0
        col1 = 0
        col2 = 0
        contador1 = 0  # Contador de movimientos para jugador 1
        contador2 = 0  # Contador de movimientos para jugador 2
        
        while ganador != 0:
            if turno == 1:
                temp = 0
                estado1 = jugadas1[fila1][col1] if col1 < len(jugadas1[fila1]) else None
                
                if estado1 is None:
                    break  # Si no hay más movimientos disponibles

                salto = 0
                
                if estado1 == estado2:
                    contador = 0
                    for i in jugadas1:
                        temp = i[col1] if col1 < len(i) else None
                        contador += 1
                        if temp != estado2:
                            fila1 = contador - 1
                            salto = 0
                            break
                        salto = 1
                    estado1 = temp
                
                if salto == 0:
                    desplazar_ficha(j1, estado1, 'red')  # Ficha roja para el jugador 1
                    col1 += 1
                    contador1 += 1  # Incrementar el contador del jugador 1
                
                turno = 2
                
                # Verificar condiciones de victoria
                if contador1 > 0 and estado1 == '25':  # Player 1 wins
                    ganador = 0
                    MessageBox.showinfo("Felicitaciones!", "Ha ganado el jugador 1")
                    reiniciar_juego()
                    return  # Salir del juego

            elif turno == 2:
                temp = 0
                estado2 = jugadas2[fila2][col2] if col2 < len(jugadas2[fila2]) else None
                
                if estado2 is None:
                    break  # Si no hay más movimientos disponibles

                salto = 0
                
                if estado2 == estado1:
                    contador = 0
                    for i in jugadas2:
                        temp = i[col2] if col2 < len(i) else None
                        contador += 1
                        if temp != estado1:
                            fila2 = contador - 1
                            salto = 0
                            break
                        salto = 1
                    estado2 = temp
                
                if salto == 0:
                    desplazar_ficha(j2, estado2, 'blue')  # Ficha azul para el jugador 2
                    col2 += 1
                    contador2 += 1  # Incrementar el contador del jugador 2
                
                turno = 1
                
                # Verificar condiciones de victoria
                if contador2 > 0 and estado2 == '21':  # Player 2 wins
                    ganador = 0
                    MessageBox.showinfo("Felicitaciones!", "Ha ganado el jugador 2")
                    reiniciar_juego()
                    return  # Salir del juego

        # Verificar si ambos han terminado sin ganar
        if contador1 > 0 and contador2 > 0 and (estado1 != '25' and estado2 != '21'):
            MessageBox.showinfo("Fin del juego", "Ninguno ganó, ambos alcanzaron sus límites de movimiento.")
            reiniciar_juego()

    elif not jugadas1 and not jugadas2:
        MessageBox.showinfo("Mensaje", "No hay jugadas ganadoras para los jugadores")
    elif not jugadas1:
        MessageBox.showinfo("Felicitaciones!", "Gana el jugador 2 por default")
    elif not jugadas2:
        MessageBox.showinfo("Felicitaciones!", "Gana el jugador 1 por default")

# Crear la pantalla y el tablero
pantalla = Screen()  # crear la pantalla
pantalla.setup(width=500, height=500)  # Establecer tamaño de la ventana

jugadas1 = []
jugadas2 = []
movj1 = cargar_jugadas(archivo="Ajedrez 5x5/jugada_t_1.txt", jugadas=jugadas1)
movj2 = cargar_jugadas(archivo="Ajedrez 5x5/jugada_t_2.txt", jugadas=jugadas2)

# Crear una tortuga para dibujar el tablero
tortuga_tablero = Turtle()
dibujar_tablero(tortuga_tablero)

# Crear tortugas para los jugadores
j1 = Turtle()
j2 = Turtle()
j1.speed(0)  # Velocidad de la tortuga más rápida para la animación
j2.speed(0)

# Ocultar las tortugas
j1.hideturtle()
j2.hideturtle()

# Iniciar el juego
iniciar_juego(jugadas1=jugadas1, jugadas2=jugadas2, movimientos=movj1)

pantalla.mainloop()  # Mantener la ventana abierta
