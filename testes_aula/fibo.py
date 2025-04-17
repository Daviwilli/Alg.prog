inicio = [0,1,1]
teste = 5
def fibo(teste):
    for j in range(2,len(inicio)):
        for i in inicio:
            if i > teste:
                break
            else:
                inicio[j] = inicio[j-1] + inicio[j-2]
    return inicio
print(fibo(teste))

            
