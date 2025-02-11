import networkx as nx
import matplotlib.pyplot as plt

def leer_jugadas(archivo):
    """Leer las jugadas desde el archivo y retornar un conjunto de transiciones."""
    transiciones = []
    with open(archivo, 'r') as f:
        for linea in f:
            estados = linea.strip().split(',')
            for i in range(len(estados) - 1):
                if estados[i].isdigit() and estados[i + 1].isdigit():  # Comprobar si ambos son numéricos
                    transiciones.append((estados[i], estados[i + 1]))
    return transiciones

def graficar_nfa(transiciones1, transiciones2):
    """Graficar el NFA a partir de las transiciones de dos jugadores."""
    G = nx.DiGraph()  # Crear un grafo dirigido

    # Añadir las transiciones del jugador 1 (verde)
    for estado_origen, estado_destino in transiciones1:
        if estado_origen.isdigit() and estado_destino.isdigit():  # Solo agregar si son numéricos
            G.add_edge(estado_origen, estado_destino, color='green')

    # Añadir las transiciones del jugador 2 (rojo)
    for estado_origen, estado_destino in transiciones2:
        if estado_origen.isdigit() and estado_destino.isdigit():  # Solo agregar si son numéricos
            G.add_edge(estado_origen, estado_destino, color='red')

    # Obtener los colores de las aristas
    colores = [G[u][v]['color'] for u, v in G.edges()]

    # Dibujar el grafo
    pos = nx.spring_layout(G)  # Posiciones para los nodos
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold', edge_color=colores)
    plt.title("Graficación del NFA")
    plt.show()

def main():
    # Leer jugadas de los archivos
    transiciones1 = leer_jugadas("Ajedrez 5x5/jugada_g_1.txt")  # Transiciones del jugador 1
    transiciones2 = leer_jugadas("Ajedrez 5x5/jugada_g_2.txt")  # Transiciones del jugador 2

    # Graficar el NFA
    graficar_nfa(transiciones1, transiciones2)

if __name__ == "__main__":
    main()
