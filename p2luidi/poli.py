def __mul__(self,p):
    tam = (len(self.poli),len(p))
    copia = [0]*(sum(tam)-1)
    if max(tam) == tam[0]:
        for i in range(tam[0][::-1]):
            for j in range(tam[1][::-1]):
                copia[i+j] += self.poli[i] * p[j]
    else:
        for i in range(tam[1][::-1]):
            for j in range(tam[0][::-1]):
                copia[j+i] += self.poli[j] *p[i]
    return polinomio(copia)