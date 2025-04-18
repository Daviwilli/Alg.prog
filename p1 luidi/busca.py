def buscar(L, X):
    if len(L) == 0:
        return -1
    elif len(L) == 1:
        return 0 if L[0] == X else -1
    
    m = len(L) // 2
    if L[m] == X:
        return m
    elif L[m] > X:
        return buscar(L[:m], X)
    else:
        resultado = buscar(L[m+1:], X)
        return m + 1 + resultado if resultado != -1 else -1

print(buscar([1, 2, 3, 4, 5, 6, 7], 6))
