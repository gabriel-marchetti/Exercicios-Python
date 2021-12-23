# Faça um programa que leia dois números m e n. O seu programa deve imprimir
# o Máximo Divisor Comum (MDC) dos números m e n. Você deve utilizar a seguinte
# regra (chamada de Algoritmo de Euclides) para calcular o MDC dos dois
# números dados:

def alg_euclides(m, n):
    if n == 0:
        return m
    else:
        return alg_euclides(n, m % n)

# Programa propriamente dito:


n = int(input('Qual o primeiro número? '))
m = int(input('Qual o segundo número? '))

print(alg_euclides(m, n))
