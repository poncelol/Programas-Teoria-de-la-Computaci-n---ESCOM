import random

def derivar_gramatica(S, pasos):
    derivaciones = [f"Paso 1: ({S})"] 
    paso_actual = 2
    while pasos > 0:
        opciones = []
        if 'S' in S:
            opciones.append('S')
        if 'A' in S:
            opciones.append('A')
        
        if not opciones:
            break
        
        eleccion = random.choice(opciones)
        
        if eleccion == 'A':
            if random.choice([True, False]): 
                S = S.replace('A', '(;eS)', 1)
                derivaciones.append(f"Paso {paso_actual}: Aplicamos A -> ;eS: ({S})")
            else:  
                S = S.replace('A', '', 1)
                derivaciones.append(f"Paso {paso_actual}: Aplicamos A -> ε: ({S})")
        elif eleccion == 'S':
            S = S.replace('S', '(iCtSA)', 1)  
            derivaciones.append(f"Paso {paso_actual}: Aplicamos S -> iCtSA: ({S})")
        
        pasos -= 1
        paso_actual += 1
    return derivaciones

def convertir_a_pseudocodigo(S):
    S = S.replace('i', 'if (').replace('C', 'cond').replace('t', ') then {').replace(';e', '} else {')
    num_abiertas = S.count('{')
    num_cerradas = S.count('}')
    S += '}' * (num_abiertas - num_cerradas)
    S = S.replace(')', ')\n').replace('{', '\n{\n').replace('}', '\n}\n')
    return S

max_derivaciones = 1000

modo = int(input("Elige el modo de ejecución (1 para manual, 2 para automático): "))

if modo == 1:
    num_derivaciones = int(input("Ingrese el número de derivaciones (hasta 1000): "))
    if num_derivaciones > max_derivaciones:
        num_derivaciones = max_derivaciones
else:
    num_derivaciones = random.randint(1, max_derivaciones)

S = 'S'
derivaciones = derivar_gramatica(S, num_derivaciones)

with open('BNC_Derivaciones.txt', 'w', encoding='utf-8') as f:
    for deriv in derivaciones:
        f.write(f"{deriv}\n")

if derivaciones:
    ultima_derivacion = derivaciones[-1].split(": ")[-1]
    pseudocodigo = convertir_a_pseudocodigo(ultima_derivacion)
    with open('BNC_Pseudocodigo.txt', 'w', encoding='utf-8') as f:
        f.write(pseudocodigo)

print("Las derivaciones se han guardado en 'derivaciones.txt'")
print("El pseudo-código se ha guardado en 'pseudocodigo.txt'")
