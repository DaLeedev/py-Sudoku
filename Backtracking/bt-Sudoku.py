from simpleai.search import CspProblem, backtrack

tabla = [
    [0, 0, 1, 3, 0, 2, 0, 0, 0],
    [0, 0, 0, 8, 1, 0, 0, 4, 2],
    [0, 9, 0, 0, 0, 0, 3, 0, 0],
    [3, 0, 7, 6, 9, 8, 1, 2, 0],
    [1, 0, 6, 2, 0, 5, 4, 7, 9],
    [5, 0, 9, 0, 4, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 6, 0, 9, 3],
    [0, 6, 4, 0, 0, 0, 2, 5, 0],
    [0, 0, 2, 0, 8, 0, 0, 0, 0]

]

variables = [(fila, col) for fila in range(9) for col in range(9)]


dominios = {}
for fila in range(9):
    for col in range(9):
        if tabla[fila][col] == 0:
            dominios[(fila, col)] = list(range(1, 10))
        else:  
            dominios[(fila, col)] = [tabla[fila][col]]


def diferentes(variables, valores):
    return valores[0] != valores[1]

#restricciones para que no haya números repetidos en la misma fila y columna

restricciones = []

for fila in range(9):
    celdas_fila = [(fila, col) for col in range(9)]
    for i in range(len(celdas_fila)):
        for j in range(i + 1, len(celdas_fila)):
            restricciones.append(((celdas_fila[i], celdas_fila[j]), diferentes ))


for col in range(9):
    celdas_col = [(fila, col) for fila in range(9)]
    for i in range(len(celdas_col)):
        for j in range(i + 1, len(celdas_col)):
            restricciones.append(((celdas_col[i], celdas_col[j]), diferentes ))

#restricciones en para cada subcuadro
for sub_fila in [0, 3, 6]:
    for sub_col in [0, 3, 6]:
        celdas_subcuadro = [(sub_fila + i, sub_col + j) for i in range(3) for j in range(3)]
        for i in range(len(celdas_subcuadro)):
            for j in range(i + 1, len(celdas_subcuadro)):
                restricciones.append(((celdas_subcuadro[i], celdas_subcuadro[j]), diferentes))

problema = CspProblem(variables, dominios, restricciones)
solucion = backtrack(problema)

if solucion:
    for fila in range(9):
        fila_solucion = [solucion[(fila, col)] for col in range(9)]
        print(fila_solucion)
else:
    print("No se encontro una solucion a este sudoku.")
