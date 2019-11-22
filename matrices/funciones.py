## En este script puedes encontrar funciones para leer, modificar e imprimir matrices (y otras cosas)

# Leer una matriz nxm elemento a elemento a partir de la entrada estándard
def lee_matriz(n, m):
    matriz = []
    for i in range(0, n):
        fila = []
        for j in range(0, m):
            fila.append(int(input()))
        matriz.append(fila)
    return matriz



# Imprime una matriz por pantalla (cada fila de la matriz aparece en una línea distinta)
def imprime_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end='  ')
        print()