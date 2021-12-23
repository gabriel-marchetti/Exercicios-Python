# Esse programa tem como intuito
# testar as funções do print()

import time
# Essa biblioteca vai servir para darmos a sensação de carregar
# ou melhor, de loading de uma função

# Façamos então

getNumber = int(input('Escolha algum número: '))

print('Processando o seu número')

for i in range(3):
    print('.')
    time.sleep(.5)

print(f'O seu número é: {getNumber}')
