class tempo():
    def __init__(self,horas,minutos,segundos):
        self.tempo = [horas,minutos,segundos]
    def __add__(self,other):
        resultado = [0,0,0]
        for i in range(len(self.tempo)):
            resultado[i] = self.tempo[i] + other.tempo[i]
        self.ajusta(resultado)
        return resultado
    def __sub__(self,other):
        resultado = [0,0,0]
        for i in range(len(self.tempo)):
            resultado[i] = self.tempo[i] - other.tempo[i]
        self.ajusta(resultado)
        return resultado
    def ajusta(self,resultado):
        if resultado[2] >= 60:
            resultado[1] += resultado[2]//60
            resultado[2] = resultado[2]%60
        if resultado[1] >= 60:
            resultado[0] += resultado[1]//60
            resultado[1] = resultado[1]%60
        for i in range(len(resultado)-1):
            if resultado[i] < 0:
                resultado[i+1] = resultado[i]*(-60) + resultado[i]
                resultado[i] = 0
        return resultado
    def __repr__(self):
        pass
A = tempo(2,0,1)
B = tempo(2,1,0)
print(A-B)