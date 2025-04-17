V = [1,5,3,2]
m = 3
menores = []
def receber(V, m, menores):
    while len(menores) < m:
        menor = V[0]
        for i in V:
            if i < menor:
                menor = i
        menores.append(menor)
        V.remove(menor)
    return menores
print(receber(V,m,menores))
