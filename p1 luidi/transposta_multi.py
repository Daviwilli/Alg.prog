def transposta(A):
    T = []
    for i in range(len(A)):
        T.append([])
        for j in range(len(A[0])):
            T[i].append(0)
    for i in range(len(A)):
        for j in range(len(A[0])):
                T[i][j] = A[j][i]
    return T
def multi(A,B):
    copia = []
    for i in range(len(A)):
        copia.append([])
        for j in range(len(B[0])):
            copia[i].append(0)
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                copia[i][j] += A[i][k]*B[k][j]
    return copia
A = [[1],[2]]
B = [[1,2]]
if len(A[0]) == len(B):
    print(multi(A,B))
else:
    print(multi(A,transposta(B)))

    