V = [1, 4, 3, 2, 6]

def devolver(V):
    for i in range(len(V)):
        for j in range(len(V)):
            if V[i] < V[j]:
                yield (V[i], V[j])  # Gerando um par (V[i], V[j])

# Convertendo o gerador em uma lista para visualizar os pares gerados
resultado = list(devolver(V))
print(resultado)
