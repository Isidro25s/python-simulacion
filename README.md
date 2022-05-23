# Simulacion de Sistemas - Python
## Tabla de Contenidos

- [Ejercicios - Introduccion a Python](#ejercicios---introduccion-a-python)
- [Generadores - Numeros Pseudoaleatorios](#generadores---numeros-pseudoaleatorios)
    - [Generar Archivos .csv](#generar-archivos-csv)
    - [Directorio de Archivos .csv](#directorio-de-archivos-csv)
- [Validadores](#validadores)
    - [Importar Archivos .csv](#importar-archivos-csv)

## Ejercicios - Introduccion a Python 
---
Ejericios practicos de Python:
- Ecuacion Cudratica
- Cadenas de Texo
- f - String
- Distancia de Hamming
- Año Bisiesto
- If
- Verificar si una persona es apta para donar sangre 


## Generadores - Numeros Pseudoaleatorios
---
Algoritmos para el calculo de numeros pseudoaleatorios:
- Algoritmo de Productos Medios
- Algoritmo Lineal
- Algoritmo Congruencial Multiplicativo
- Algoritmo Congruencial Aditivo
- Algoritmo Congruencial Cuadratico

### Generar Archivos .csv
Hay que establecer el nombre del .csv que se va a generar en la variable "archivo"

**Ejemplo:**
```py
from guardarNumeros import guardarNumeros

# Agregar el nombre del archivo en la siguiente variable
archivo = 'numerosPseudo-1.csv'
```

#### Directorio de Archivos .csv
Todos los archivos .csv generados seran guardados en el directorio *files*

## Validadores
---
Pruebas para numeros pseudoaleatorios:
- Prueba de Medias
- Prueba de Varianza
- Pruebas de Uniformidad
    - Prueba Chi Cuadrada
    - Prueba Kolmogorov – Smirnov
- Pruebas de Independencia
    - Prueba de Corridas Arriba y Debajo de la Media
    - Prueba de Poker
    - Prueba de Series

### Importar Archivos .csv
Hay que establecer el nombre del .csv en la variable "archivo"

**Ejemplo:**
```py
from extraerNumeros import extraerNumeros

# Agregar el nombre del archivo en la siguiente variable
archivo = 'numerosPseudo-1.csv'
```
*Los numeros numeros pseudoaleatorios que esten guardados en el archivo .csv seran guardados en una lista*