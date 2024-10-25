# Eliminación de Recursividad y Cálculo de PRIMEROS, SIGUIENTES, y PREDICCIÓN

Este repositorio contiene un programa en Python que elimina la recursividad por la izquierda en gramáticas, y calcula los conjuntos de **PRIMEROS**, **SIGUIENTES**, y **PREDICCIÓN** para las reglas de la gramática.

## Archivos en el proyecto

1. **gramatica.py**: 
   El archivo principal que contiene el código Python para:
   - Leer una gramática desde un archivo.
   - Eliminar la recursividad por la izquierda.
   - Calcular los conjuntos de PRIMEROS, SIGUIENTES, y PREDICCIÓN.
   - Imprimir los resultados en la terminal.

2. **gramatica.txt**:
   Un archivo de texto que contiene la gramática que quieres procesar. Este archivo puede ser modificado para probar diferentes gramáticas. Las reglas de la gramática deben estar en el formato:

   ```plaintext
   Regla -> producción1 | producción2 | ... | producciónN
