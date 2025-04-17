def primo(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
def rotacao(numero):
    rotacoes = []
    n_Numero = str(numero)
    for i in range(len(str(numero))):
        rot = n_Numero[i:] + n_Numero[:i]
        if primo(int(rot)) == True:
            continue
        else:
            return False
    return True
def primos_circulares(numero):
    pr = []
    for i in range(2, numero+1):
        if rotacao(i) and primo(i):
            pr.append(i)
    return pr
                
print(primos_circulares(101))
        


        