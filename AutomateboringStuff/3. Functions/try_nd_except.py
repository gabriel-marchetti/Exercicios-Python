# Quando tivermos um programa onde claramente temos um caso
# indesejável, então podemos usar a função do python dita
# try_and_except.
# Vamos supor que desejamos fazer uma função que faça uma
# divisão, então podemos fazer a seguinte estrutura de
# código

def divisão(divideBy):
    return 42 / divideBy

# veja que nesse caso, se dermos o argumento zero, então
# iremos ganhar um erro no terminal

# por conta disso existem dois métodos que podemos usar
# para resolver esse caso


def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Erro: Argumento Inválido')


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

# Outro modo de escrevermos é através de:


def spam2(divideBy):
    return 42 / divideBy


try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')
