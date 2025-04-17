A = [1,5,7,9,2,1]
copia = []
m = 3 
while len(copia) != m:
    for i in A:
        menor = A[0]
        if i < menor:
            menor = i
    copia.append(menor)
    A.remove(i)
print(copia)