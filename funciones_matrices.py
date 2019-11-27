## En este script puedes encontrar funciones para leer, modificar e imprimir matrices (y otras cosas)

from random import randint


# Leer una matriz nxm elemento a elemento a partir de la entrada estándard
def lee_matriz(n, m):
    M = []
    for i in range(0, n):
        fila = []
        for j in range(0, m):
            fila.append(int(input()))
        M.append(fila)
    return M



# Imprime una matriz por pantalla (cada fila de la matriz aparece en una línea distinta)
def imprime_matriz(M):
    '''
    for fila in M:
        for elemento in fila:
            if int(elemento) == elemento:
                elemento = int(elemento)
            print(elemento, end='  ')
        print()
    '''
    def format_value(x):
        if x == int(x):
            x = int(x)
        return str(x)
    
    from IPython.display import Math, display
    
    text = ''
    text += r'\quad\begin{pmatrix}'+'\n'
    text += (r'\\' + '\n').join([' & '.join(map(format_value, fila)) for fila in M])
    text += r'\end{pmatrix}\quad'+'\n'
    display(Math(text))
    
       
       
# Crea una matriz nxm de numeros enteros alatorios entre 0 y k inclusive
def matriz_aleatoria(n, m, k):
    M = []
    for i in range(0, n):
        fila = []
        for j in range(0, m):
            fila.append(randint(0, k))
        M.append(fila)
    return M
        
    

# Devuelve la matriz identidad de orden n
def matriz_identidad(n):
    M = []
    for i in range(0, n):
        fila = []
        for j in range(0, n):
            fila.append(1 if i == j else 0)
        M.append(fila)
    return M
    
    

# Esta función toma como argumento una matriz de tamaño nxm y devuelve una submatriz de n-1xm-1 que resulta de eliminar la fila i-ésima y la columna j-ésima
def submatriz(M, i, j):
    n = len(M)
    S = []
    for a in range(0, n):
        if a == i:
            continue
            
        fila = []
        for b in range(0, n):
            if b == j:
                continue
            fila.append(M[a][b])
        S.append(fila)
        
    return S


# Producto entre un escalar y una matriz de orden nxm
def producto_escalar(M, k):    
    S = []
    n, m = len(M), len(M[0])
    
    for i in range(0, n):
        fila = []
        for j in range(0, m):
            fila.append(M[i][j] * k)
        S.append(fila)
    
    return S



# Producto matricial entre una matriz A nxm y otro B de tamaño mxp. El resultado es una matriz
# de tamaño nxp
def producto_matricial(A, B):
    n, m, p = len(A), len(A[0]), len(B[0])
    C = []
    for i in range(0, n):
        fila = []
        for j in range(0, p):
            s = 0
            for k in range(0, m):
                s += A[i][k] * B[k][j]
            fila.append(s)
        C.append(fila)
    return C



# Devuelve el determinante de una matriz cuadrada de orden n
def determinante(M):
    n = len(M)
    
    if n == 1:
        # matriz de orden 1
        return M[0][0]
    
    if n == 2:
        # matriz de orden 2
        return M[0][0] * M[1][1] - M[1][0] * M[0][1]
    
    # matriz de orden superior a 2
    D = 0
    for k in range(0, n):
        D += (1 - 2 * (k % 2)) * M[0][k] * determinante( submatriz(M, 0, k) )
    return D



# Calcula la matriz de cofactores de una matriz de orden n
def cofactores(M):
    S = []
    n = len(M)
    for i in range(0, n):
        fila = []
        for j in range(0, n):
            s = ((1 - i % 2) * 2 - 1) * ((1 - j % 2) * 2 - 1) * determinante(submatriz(M, i, j))
            fila.append(s)
        S.append(fila)
    return S



# Calcula la transpuesta de una matriz de tamaño nxm
def transpuesta(M):
    S = []
    m, n = len(M), len(M[0])
    for i in range(0, n):
        fila = []
        for j in range(0, m):
            fila.append(M[j][i])
        S.append(fila)
    return S


# Calcula la matriz adjunta de una matriz no singular de orden n
def adjunta(M):
    return transpuesta(cofactores(M))


# Calcular la inversa de un matriz no singular de orden n
def inversa(M):
    return producto_escalar(adjunta(M), 1 / determinante(M))


