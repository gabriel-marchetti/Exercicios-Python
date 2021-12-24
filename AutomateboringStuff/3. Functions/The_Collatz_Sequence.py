# Esse programa tem como objetivo recriar a conjectura de Collatz
# Dado isso, nosso objetivo é criar uma função que tenha o seguinte
# comportamento. Dada uma entrada, que é um número
# se esse número for par, então a função deve imprimir number // 2
# e retornar o seu valor
# Agora, se number for ímpar, então a sua função deve retornar
# 3 * number + 1

# Vamos então fazer a nossa função

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


numberUser = int(
    input('Qual número você deseja colocar no processo de Collatz? '))

print(numberUser)
while numberUser != 1:
    numberUser = collatz(numberUser)
    print(numberUser)
