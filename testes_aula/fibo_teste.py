# "Na matemática, a sucessão de Fibonacci (ou sequência de Fibonacci), é uma sequência de números inteiros, começando normalmente por 0 e 1, na qual cada termo subsequente corresponde à soma dos dois anteriores.

# Os números de Fibonacci são, portanto, os números que compõem a seguinte sequência:

# 0,1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, ... " Texto tirado da Wikipedia.org

# Leia um número inteiro não negativo n.

# Crie uma lista (list) com todos os números da sequencia de Fibonacci até n. Imprima a lista.

# Depois (em outra linha) imprima a soma dos elementos da lista.
a = int(input())
inicio = [0,1,1]
adicionar = 0
soma = 0
def fibo(numero):
    global adicionar
    global soma
    global inicio
    if numero == 0:
        inicio = [0]
    for i in range(numero):
        adicionar = inicio[-1] + inicio[-2]
        inicio.append(adicionar)
        for j in inicio:
            if j > numero:
                inicio.remove(inicio[-1])
                break
    for i in inicio:
        soma += i
    return inicio, soma
print(fibo(a))