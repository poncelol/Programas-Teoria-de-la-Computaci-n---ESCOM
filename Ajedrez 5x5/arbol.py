import networkx as nx
import matplotlib.pyplot as plt

# Función para leer y filtrar rutas y movimientos de cada archivo
def leer_y_filtrar_rutas_y_movimientos(archivo):
    secuencias_movimientos = []
    secuencias_rutas = []
    lineas_validas = []

    with open(archivo, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                # Verificar si la línea tiene una coma para dividirla en dos partes
                if ',' in line:
                    partes = line.split(',')
                    if len(partes) >= 2:
                        movimientos = partes[0].strip()
                        ruta = partes[1:]  # Ruta numérica
                        
                        # Filtrar líneas según el estado final
                        if ruta.count('25') >= 1 or ruta.count('21') >= 1:
                            # Encontrar el índice de la primera ocurrencia de 25 o 21
                            indice_final = min(
                                (ruta.index('25') if '25' in ruta else len(ruta)),
                                (ruta.index('21') if '21' in ruta else len(ruta))
                            )
                            # Mantener solo la parte de la ruta hasta el índice final
                            ruta_corregida = ruta[:indice_final + 1]  # Incluir el estado final
                        else:
                            ruta_corregida = ruta

                        secuencias_movimientos.append(movimientos)
                        secuencias_rutas.append(ruta_corregida)
                        lineas_validas.append(f"{movimientos}," + ','.join(ruta_corregida))  # Agregar la línea válida
                else:
                    print(f"Formato no esperado en la línea: {line}")
    
    # Escribir líneas válidas de vuelta al archivo
    with open(archivo, 'w') as f:
        for linea in lineas_validas:
            f.write(linea + '\n')
    
    return secuencias_movimientos, secuencias_rutas

# Función para graficar el árbol de movimientos
def graficar_ruta(movimientos, rutas, jugador):
    G = nx.DiGraph()
    estado_inicial, estado_final = (1, 25) if jugador == 1 else (5, 21)
    
    # Añadir nodo inicial y final
    G.add_node(estado_inicial)  # Nodo inicial
    G.add_node(estado_final)    # Nodo final
    
    # Crear las transiciones según los movimientos y rutas
    for secuencia_mov, secuencia_ruta in zip(movimientos, rutas):
        estado_actual = estado_inicial
        for transicion in secuencia_ruta:
            try:
                transicion_int = int(transicion)
                if transicion_int:  # Asegurarse de que la transición no sea cero
                    G.add_edge(estado_actual, transicion_int)
                    estado_actual = transicion_int
            except ValueError:
                print(f"Transición no válida: {transicion}")
    
    # Solo agregar la arista de entrada a los estados finales
    if estado_actual != estado_final:
        G.add_edge(estado_actual, estado_final)
    
    return G

# Función para dibujar y guardar el grafo
def dibujar_y_guardar_grafo(G, jugador):
    plt.figure(figsize=(12, 10))
    
    # Usar el spring_layout con mayor separación entre nodos
    pos = nx.spring_layout(G, k=2, iterations=50)  # Aumentar k para más separación
    labels = {nodo: str(nodo) for nodo in G.nodes()}  # Etiquetar nodos con su identificador
    
    # Dibujar nodos y bordes (edges) con flechas
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=10, font_weight='bold', edge_color='gray', width=1.0, arrows=True)
    
    # Añadir etiquetas sin color rojo
    nx.draw_networkx_labels(G, pos, labels, font_size=12)  # Eliminado font_color='red'
    
    # Guardar en PNG
    plt.title(f"Árbol de Movimientos del Jugador {jugador}")
    plt.savefig(f"jugador_{jugador}_arbol_movimientos.png", bbox_inches='tight')
    plt.close()

# Leer y filtrar archivos .txt del jugador 1 y jugador 2
movimientos_j1, rutas_j1 = leer_y_filtrar_rutas_y_movimientos('Ajedrez 5x5/jugada_g_1.txt')
movimientos_j2, rutas_j2 = leer_y_filtrar_rutas_y_movimientos('Ajedrez 5x5/jugada_g_2.txt')


# Graficar y guardar árbol de movimientos del Jugador 1
G1 = graficar_ruta(movimientos_j1, rutas_j1, jugador=1)
dibujar_y_guardar_grafo(G1, jugador=1)

# Graficar y guardar árbol de movimientos del Jugador 2
G2 = graficar_ruta(movimientos_j2, rutas_j2, jugador=2)
dibujar_y_guardar_grafo(G2, jugador=2)

print("Se han generado los archivos PNG para ambos jugadores y los archivos .txt han sido actualizados.")
