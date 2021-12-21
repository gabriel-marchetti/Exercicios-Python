import random
import time

# Esse exercício tem como objetivo criar um jogo onde o computador pode
# escolher um número entre 1 a 20. Dada a escolha do computador
# o objetivo do usuário é tentar adivinhar qual número
# foi escolhido pelo computador


# Escolha do número feita pelo computador
secretNumber = random.randint(1, 20)

print('Estou pensando em um valor entre 1 e 20...')
time.sleep(1)
print('Você consegue adivinhar?')
time.sleep(1)

flag = True
while flag:
    numberGuess = int(input('Qual número você está pensando? '))
    if numberGuess < secretNumber:
        print('hmmm....')
        time.sleep(1)
        # Essa variável aqui tem apenas a função de gerar
        # alguns diálogos extras
        diálogo_1 = random.randint(1, 3)
        if diálogo_1 == 1:
            print('Tente uma valor mais alto!')
        elif diálogo_1 == 2:
            print('Esse valor é meio baixo...')
        elif diálogo_1 == 3:
            print('É um número maior!')
    elif numberGuess > secretNumber:
        print('hmmm....')
        time.sleep(1)
        diálogo_2 = random.randint(1, 3)
        if diálogo_2 == 1:
            print('Tente uma valor mais baixo agora!')
        elif diálogo_2 == 2:
            print('Esse valor é meio alto...')
        elif diálogo_2 == 3:
            print('É um número menor!')
    else:
        flag = False

print('Você adivinhou que o valor que estou pensando é: ' + str(secretNumber))
print('Parabéns!!!! ')
