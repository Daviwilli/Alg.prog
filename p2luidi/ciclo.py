class ciclo():
    def __init__(self,recebido):
        self.centro = recebido[0]
        self.raio = recebido[1]
    def ponto_in_ciclo(self,ponto):
        if (self.raio**(2)) == (self.centro[0] - ponto[0])**(2) + (self.centro[1] - ponto[1])**(2):
            return True
        else:
            return False
    def rect_in_ciclo(self,t2):
        for i in t2:
            if self.ponto_in_ciclo(i) == False:
                return False
        else:
            return True
    
#inputs
n = eval(input())
t1,t2 = n[0],n[1]
objeto = ciclo(t1)
if len(t2) == 1:
    print(objeto.ponto_in_ciclo(t2))
if len(t2) == 4:
    print(objeto.rect_in_ciclo(t2))
