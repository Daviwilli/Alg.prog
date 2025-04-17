class Forca():
    def __init__(self,palavra):
        self.palavra = palavra
        self.tabuleiro = ["_"]*len(palavra)
        self.tentativas = 9
        self.vitoria = False
    def joga(self,x):
        if self.vitoria == True:
            print("a palavra era:\n")
            return self.tabuleiro
        if x not in self.palavra:
            self.falha()
        for i,j in enumerate(self.palavra):
            if x == j:
                self.tabuleiro[i] = x
        self.ganhador()
        return self.tabuleiro
    def __repr__(self):
        return str(self.tabuleiro)
    def ganhador(self):
        if list(self.palavra) == self.tabuleiro:
            self.vitoria = True
    def falha(self):
        self.tentativas -= 1
        if self.tentativas == 0:
            print("Você perdeu")
A = Forca("coelho")
chutes = "coelh"
for i in chutes:
    print(A.joga(i))
    