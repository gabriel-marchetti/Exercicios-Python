# Esse programa tem como objetivo recriar a conjectura de Collatz
# Dado isso, nosso objetivo é criar uma função que tenha o seguinte
# comportamento. Dada uma entrada, que é um número
# se esse número for par, então a função deve imprimir number // 2
# e retornar o seu valor
# Agora, se number for ímpar, então a sua função deve retornar
# 3 * number + 1
# Nesse caso também queremos identificar se o usuário colocou uma
# variável do tipo inteira, pois senão, a conjectura não funcionaria

# Vamos então fazer a nossa função
import sys


def collatz(number):
    # Entradas
    #   number: um número a escolha do usuário
    # Saídas
    #   se number for par, return number // 2
    #   se number for ímpart, return 3 * number + 1
    if number % 2 == 0:
        # Então o nosso número é par
        return number // 2
    else:
        # Nesse caso ele será ímpar
        return 3 * number + 1

# Estrutura do código, isto é, no escopo global
# Mesmo que não seja recomendável, ainda sim vou fazer
# só para não ter que usar uma função main() :P


try:
    numberUser = abs(int(
        input('Qual número você deseja colocar no processo de Collatz? ')))
    if numberUser == 0:
        print('Zero gera uma sequência sem Fim.')
        sys.exit()
    print(numberUser)
    while abs(numberUser) != 1:
        numberUser = collatz(numberUser)
        print(numberUser)

except ValueError:
    print('Isso não é uma variável inteira')

# Obs: Foi dito no problema que essa sequência funciona para qualquer inteiro
# Entretando testando para o valor '-150' eu obtive um ciclo infinito
# Dito isto, no WikiPedia e em algumas outras fontes, acho que de fato não
# funciona para todos os números inteiros, mas sim para números inteiros
# postivos
