# Eliminación de Recursividad y Cálculo de PRIMEROS, SIGUIENTES, y PREDICCIÓN

## Archivos en el proyecto

1. **gramatica.py**: 
   El archivo principal que contiene el código Python para:
   - Leer una gramática desde un archivo.
   - Eliminar la recursividad por la izquierda.
   - Calcular los conjuntos de PRIMEROS, SIGUIENTES, y PREDICCIÓN.
   - Imprimir los resultados en la terminal.

2. **gramatica.txt**:
   Un archivo de texto que contiene la gramática que quieres procesar. Este archivo puede ser modificado para probar diferentes gramáticas. Las reglas de la gramática deben estar en el formato:

## Ejecucion

 - Para la ejecucion debemos tener instalado python3
   -> python3 gramatica.py
 - La salida varia dependiendo de la gramativa:
   
   Si tenemos la siguiente gramatica:
   
      ```X -> X p | X q | r s | r t
      ```Y -> Y u | v | v w
      ```Z -> Z x | y z | y w
      
   La salida deberia ser algo asi:

      Gramática después de eliminar recursividad por la izquierda:
      
X -> r s X' | r t X'
X' ->  p X' |  q X' | ε
Y -> v Y' | v w Y'
Y' ->  u Y' | ε
Z -> y z Z' | y w Z'
Z' ->  x Z' | ε

Conjuntos de PRIMEROS:
PRIMERO(X) = {'r'}
PRIMERO(X') = {'p', 'ε', 'q'}
PRIMERO(Y) = {'v'}
PRIMERO(Y') = {'ε', 'u'}
PRIMERO(Z) = {'y'}
PRIMERO(Z') = {'x', 'ε'}

Conjuntos de SIGUIENTES:
SIGUIENTE(X) = {'$'}
SIGUIENTE(X') = {'$'}
SIGUIENTE(Y) = set()
SIGUIENTE(Y') = set()
SIGUIENTE(Z) = set()
SIGUIENTE(Z') = set()

Conjuntos de PREDICCIÓN:
PREDICCIÓN(X) = [{'r'}, {'r'}]
PREDICCIÓN(X') = [{'p'}, {'q'}, {'$'}]
PREDICCIÓN(Y) = [{'v'}, {'v'}]
PREDICCIÓN(Y') = [{'u'}, set()]
PREDICCIÓN(Z) = [{'y'}, {'y'}]
PREDICCIÓN(Z') = [{'x'}, set()]


      


