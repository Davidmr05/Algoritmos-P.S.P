# Función para eliminar recursividad por la izquierda
def eliminar_recursividad_izquierda(gramatica):
    gramatica_nueva = {}
    for regla, producciones in gramatica.items():
        nuevas_producciones = []
        producciones_recursivas = []
        for produccion in producciones:
            if produccion.startswith(regla):
                producciones_recursivas.append(produccion[1:])
            else:
                nuevas_producciones.append(produccion)
        if producciones_recursivas:
            nueva_variable = regla + "'"
            gramatica_nueva[regla] = [prod + " " + nueva_variable for prod in nuevas_producciones]
            gramatica_nueva[nueva_variable] = [prod + " " + nueva_variable for prod in producciones_recursivas] + ['ε']
        else:
            gramatica_nueva[regla] = producciones
    return gramatica_nueva

# Función para calcular el conjunto de PRIMEROS
def calcular_primeros(gramatica):
    primeros = {regla: set() for regla in gramatica}

    def calcular_primeros_regla(regla):
        for produccion in gramatica[regla]:
            simbolo = produccion.split()[0]
            if simbolo.islower():  # Terminal
                primeros[regla].add(simbolo)
            else:  # No terminal
                for terminal in calcular_primeros_regla(simbolo):
                    primeros[regla].add(terminal)
        return primeros[regla]

    for regla in gramatica:
        calcular_primeros_regla(regla)
    
    return primeros

# Función para calcular el conjunto de SIGUIENTES
def calcular_siguientes(gramatica, primeros):
    siguientes = {regla: set() for regla in gramatica}
    siguientes[list(gramatica.keys())[0]].add('$')  # El símbolo inicial contiene $

    def agregar_siguientes(no_terminal, regla):
        for produccion in gramatica[regla]:
            if no_terminal in produccion.split():
                produccion_partida = produccion.split()
                index = produccion_partida.index(no_terminal)
                if index == len(produccion_partida) - 1:
                    siguientes[no_terminal] |= siguientes[regla]
                else:
                    siguiente_simbolo = produccion_partida[index + 1]
                    if siguiente_simbolo.islower():
                        siguientes[no_terminal].add(siguiente_simbolo)
                    else:
                        siguientes[no_terminal] |= primeros[siguiente_simbolo]
                        if 'ε' in primeros[siguiente_simbolo]:
                            siguientes[no_terminal] |= siguientes[regla]

    for regla in gramatica:
        for no_terminal in gramatica:
            agregar_siguientes(no_terminal, regla)
    
    return siguientes

# Función para calcular los conjuntos de PREDICCIÓN
def calcular_predicciones(gramatica, primeros, siguientes):
    predicciones = {}
    
    for regla, producciones in gramatica.items():
        predicciones[regla] = []
        for produccion in producciones:
            if produccion == 'ε':
                predicciones[regla].append(siguientes[regla])
            else:
                primer_simbolo = produccion.split()[0]
                if primer_simbolo.islower():
                    predicciones[regla].append({primer_simbolo})
                else:
                    conjunto_prediccion = primeros[primer_simbolo] - {'ε'}
                    if 'ε' in primeros[primer_simbolo]:
                        conjunto_prediccion |= siguientes[regla]
                    predicciones[regla].append(conjunto_prediccion)

    return predicciones

# Función para leer la gramática desde un archivo
def leer_gramatica(archivo):
    gramatica = {}
    with open(archivo, 'r') as file:
        for linea in file:
            if '->' in linea:
                regla, producciones = linea.split('->')
                producciones = producciones.split('|')
                gramatica[regla.strip()] = [prod.strip() for prod in producciones]
    return gramatica

# Main
if __name__ == '__main__':
    # Lee la gramática desde el archivo
    gramatica = leer_gramatica("gramatica.txt")
    
    # Eliminar recursividad por la izquierda
    gramatica_sin_recursividad = eliminar_recursividad_izquierda(gramatica)

    # Cálculo de conjuntos de PRIMEROS, SIGUIENTES, y PREDICCIÓN
    primeros = calcular_primeros(gramatica_sin_recursividad)
    siguientes = calcular_siguientes(gramatica_sin_recursividad, primeros)
    predicciones = calcular_predicciones(gramatica_sin_recursividad, primeros, siguientes)

    # Imprimir los resultados
    print("\nGramática después de eliminar recursividad por la izquierda:")
    for regla, producciones in gramatica_sin_recursividad.items():
        print(f"{regla} -> {' | '.join(producciones)}")

    print("\nConjuntos de PRIMEROS:")
    for regla, conjunto in primeros.items():
        print(f"PRIMERO({regla}) = {conjunto}")

    print("\nConjuntos de SIGUIENTES:")
    for regla, conjunto in siguientes.items():
        print(f"SIGUIENTE({regla}) = {conjunto}")

    print("\nConjuntos de PREDICCIÓN:")
    for regla, conjunto in predicciones.items():
        print(f"PREDICCIÓN({regla}) = {conjunto}")
