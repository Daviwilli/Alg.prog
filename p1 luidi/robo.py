A = [
    [0,1,0],
    [0,0,1],
    [1,0,0]
]
i = 0
j = 0
caminho = [(i,j)]
def ir_baixo(A,i,j,caminho):
    i += 1
    A[i][j] = 2
    caminho.append((i,j))
    return i,j
def ir_lado(A,i,j,caminho):
    j += 1
    A[i][j] = 2
    caminho.append((i,j))
    return i,j
def verifica(A):
    global i,j,caminho
    while i < len(A)-1 or j < len(A[0])-1:
        if i + 1 < len(A) and A[i+1][j] == 0:
            i,j = ir_baixo(A,i,j,caminho)
        elif  j +1 < len(A[0]) and A[i][j+1] == 0:
            i,j = ir_lado(A,i,j,caminho)
        else:
            return False
    return caminho
print(verifica(A))

