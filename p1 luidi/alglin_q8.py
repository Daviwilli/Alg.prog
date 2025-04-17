entrada = eval(input())
T, incerteza = entrada

def t_quadrado(T):
    t_quadrado = ((T)**2)/(4*(3.1415**2))
    return t_quadrado


def incerteza_propagacao(T, incerteza):
    inc_propagacao = ((T)/(2*(3.1415**2))) * incerteza
    return inc_propagacao

print(t_quadrado(T), incerteza_propagacao(T, incerteza))
