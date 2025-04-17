V = [1,4,3,2,6]
def devolver(V):
    for i in range(len(V)):
        for j in range(len(V)):
            if V[i] < V[j]:
                yield (V[i],V[j])
retultado = list(devolver(V))
print(retultado)