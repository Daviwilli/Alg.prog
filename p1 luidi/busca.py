def marco_doido(L,X):
    if len(L) == 0:
       return -1
    elif len(L) == 1:
        if L[0] == X:
            return 0
        else:
            return -1
    m = len(L)//2
    if L[m] == X:
        return m 
    if L[m] > X: return marco_doido(L[:m],X)
    return m+ marco_doido(L[m+1],X)
print(marco_doido([1,2,3,4,5,6,7],6))

def marco_doido(L,X):
    if len(L) == 0: return -1
    def marco_doido_revan(L,X,i):
        if len(L) <= i: return -1
        if L[i] > x: return marco_doido_revan(L,X,i)

    if len(L) == 0:
       return -1
    elif len(L) == 1:
        if L[0] == X:
            return 0
        else:
            return -1
    m = len(L)//2
    if L[m] == X:
        return m 
    if L[m] > X: return marco_doido(L[:m],X)
    return m+ marco_doido(L[m+1],X)
print(marco_doido([1,2,3,4,5,6,7],6))
