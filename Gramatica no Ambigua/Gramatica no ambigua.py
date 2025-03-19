import random

def generar_parentesis_balanceados(n):
    if n % 2 != 0:
        n += 1
    parens = ['('] * (n // 2) + [')'] * (n // 2)
    random.shuffle(parens)
    return ''.join(parens)

def procesar_gramatica(cadena_entrada):
    pasos = "B"
    output = []
    i = 0
    posicion = 0
    bandera = 0
    contador = 1

    output.append("Evaluacion de la gramatica:")
    if not cadena_entrada:
        return 'Cadena de entrada invalida.'

    while True:
        output.append("-------------------------------------\nPaso : " + str(contador))
        if i < len(cadena_entrada) and bandera == 0:
            subcadena = cadena_entrada[i:]
            output.append("Cadena generada: " + subcadena + "     " + pasos + ". <--- Pasos de la derivacion mas a la izquierda.")
            output.append("Simbolo siguiente: " + cadena_entrada[i] + '.')
        elif cadena_entrada == 'ε':
            output.append("Cadena generada:  E     " + pasos + ". <--- Pasos de la derivacion mas a la izquierda.")
            output.append("Simbolo siguiente:  E.")

        for simbolo in pasos:
            if simbolo == "B":
                derivacionMasIzquierda = "B"
                break
            elif simbolo == "R":
                derivacionMasIzquierda = "R"
                break
            posicion += 1
        
        if derivacionMasIzquierda == 'B' and cadena_entrada[i] == '(':
            index = posicion
            pasos = pasos[:index] + '(RB' + pasos[index+1:]
            output.append("Regla aplicada: B --> (RB")
        elif derivacionMasIzquierda == 'B' and cadena_entrada[i] == '':
            index = posicion
            pasos = pasos[:index] + '' + pasos[index+1:]
            output.append("Regla aplicada: B --> E")
        elif derivacionMasIzquierda == 'R' and cadena_entrada[i] == ')':
            index = posicion
            pasos = pasos[:index] + ')' + pasos[index+1:]
            output.append("Regla aplicada: R --> )")
        elif derivacionMasIzquierda == 'R' and cadena_entrada[i] == '(':
            index = posicion
            pasos = pasos[:index] + '(RR' + pasos[index+1:]
            output.append("Regla aplicada: R --> (RR")
        elif derivacionMasIzquierda == 'B' and cadena_entrada == 'ε':
            index = posicion
            pasos = pasos[:index] + '' + pasos[index+1:]
            output.append("Regla aplicada: B --> E")
            output.append("\n-------------------------------------\nPaso : " + str(contador + 1))
            output.append(pasos + "  <--- Evaluacion resultante.")
            output.append("Exitosa. Cadena valida")
            break
        elif derivacionMasIzquierda == 'R' and cadena_entrada == 'ε':
            output.append("Regla aplicada: R --> E")
            output.append("\n-------------------------------------\nPaso : " + str(contador + 1))
            output.append(pasos + "  <--- Evaluacion resultante.")
            output.append("Error: Fuera de condicionales. Cadena invalida")
            break

        posicion = 0
        i += 1
        contador += 1
        if i == len(cadena_entrada) or bandera == 1:
            bandera = 1
            i = 0
            cadena_entrada = 'ε'

    return "\n".join(output)

# Main
opcion_entrada = input("Deseas ingresar una cadena manualmente (1) o generarla automaticamente (2)? ")

if opcion_entrada == '1':
    cadena_entrada = input("Ingresa una cadena de parentesis balanceados: ")
    if len(cadena_entrada) > 1000:
        print("La cadena ingresada supera los 1000 caracteres. El programa se cerrara.")
        exit()
elif opcion_entrada == '2':
    numero = random.randint(1, 1000)
    print("Tamano de la cadena escogido aleatoriamente: " + str(numero))
    cadena_entrada = generar_parentesis_balanceados(numero)
    print("Cadena generada automaticamente:", cadena_entrada)
else:
    print("Opcion invalida. El programa se cerrara.")
    exit()

derivacion = procesar_gramatica(cadena_entrada)
with open('Gramatica_no_ambigua.txt', 'w') as archivo:
    archivo.write(derivacion.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u'))

print("\n\nDerivacion resultante:\n", derivacion)
