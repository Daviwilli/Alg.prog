class Intervalo():
    def __init__(self,a,b):
        self.a = a 
        self.b = b
        self.tudo = [a,b]
        self.inter = [min(self.tudo),max(self.tudo)]
    def uniao(self,other):
        return [self.inter[0], other.inter[1]]
    def intersecao(self,other):
        minimos = [min(self.tudo), min(other.tudo)]
        maximos = [max(self.tudo), max(other.tudo)]
        conjunto = [max(minimos),min(maximos)]
        if conjunto[0] > conjunto[1]:
            raise ValueError
        return conjunto
    def __repr__(self):
        return f'Intervalo({self.inter[0]}, {self.inter[1]})'
def adiciona(l,i):
    for k,j in enumerate(l):
        try:
            x = i.intersecao(j)
            l[k] = i.uniao(j)
            return l
        except ValueError:
            pass
    l.append(i)
    return l
        
#inputs
n = ((4,1),(10,2),(2,10),((5,6),(7,9)))
e1,e2,e3,e4 = n
print(Intervalo(e1[0],e1[1]).uniao(Intervalo(e2[0],e2[1])))
print(Intervalo(e1[0],e1[1]).intersecao(Intervalo(e3[0],e3[1])))
l = [Intervalo(e1[0],e1[1])]
for i in e4:
    l = adiciona(l,Intervalo(i[0],i[1]))
print(l)