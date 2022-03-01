import math


def sign(a, b):
    # Essa função tem o objetivo de retornar o valor dos números
    return a*b/abs(a*b)


def f(x):
    # Função usada para estimar a raiz
    return math.cos(math.pi/2*x)-x


def bissection(xl, xr, tol):
    # Essa função tem como objetivo executar o método da bijeção
    # que decorre diretamente do teorema do valor intermediário
    # Entradas:
    # xl: valor inicial
    # xr: valor final
    # tol: tolerância
    # Saídas:
    # c: melhor respostas encontrada pelo algoritmo
    n = 1
    n_max = 150  # número de iterações a serem feitas
    while n <= n_max:
        error = abs(xl-xr)/2  # Erro relacionado à tolerância
        c = (xr+xl)/2  # Tentativa de encontrar raiz
        if f(c) == 0 or error < tol:
            # Nesse caso temos a solução encontrada
            print("A solução encontrada foi:", c)
            return c

        n = n + 1
        if sign(f(c), f(xl)) >= 0:
            xl = c
        else:
            xr = c
    print("A melhor resposta encontrada foi: ", c)
    return c


xl = 0
xr = 1
tol = 0.0000001

bissection(xl, xr, tol)
