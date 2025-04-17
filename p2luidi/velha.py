class Velha():
    def __init__(self):
        self.tamanho = [1,2,3,4,5,6,7,8,9]
        self.turno = 0
    def verifica(self,x):
        if self.tamanho[x-1] not in ["0","X"]:
            return True
        else:
            return False
    def joga(self,x):
        if self.verifica(x) == True:
            self.tamanho[self.tamanho.index(x)] = self.vez(self.turno)
            self.turno += 1
            if self.ganhador() == True:
                print("Ganhador")
                return True

        return self.tamanho
    def vez(self,turno):
        if turno%2 == 0:
            return "X"
        else:
            return "0"
    def ganhador(self):
        for i in [0,3,6]:
            for j in range(0,2):
                if self.tamanho[i+j] != self.tamanho[i+j+1]:
                    return False
                else:
                    return True
tabu = Velha()
jogadas = [1,6,2,5,3,8]
for i in jogadas:
    print(tabu.joga(i))
    if tabu.joga(i) == True:
        break



