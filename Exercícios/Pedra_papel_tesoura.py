import random
import time
# Esse programa tem a tentativa de simulador um jogo
# de pedra, papel e tesoura com o computador

Tentativas = int(input('Quantas vezes você quer jogar comigo? '))

print('-'*40)
print('Então vamos jogar ', str(Tentativas), ' vezes!!')
time.sleep(1)
print('As regras são:')
time.sleep(1)
print('digite (r) para pedra')
print('digite (p) para papel')
print('digite (s) para tesoura')
print('-'*40)


i = 0
empate = 0
vitoria = 0
derrota = 0
while i < Tentativas:
    playerGuess = input('Qual a sua jogada? ')
    computerGuess = random.randint(1, 3)
    if playerGuess == 'r':
        if computerGuess == 1:
            print('Empate')
            empate += 1
        elif computerGuess == 2:
            print('Derrota')
            derrota += 1
        else:
            print('Vitória')
            vitoria += 1
    if playerGuess == 'p':
        if computerGuess == 2:
            print('Empate')
            empate += 1
        elif computerGuess == 3:
            print('Derrota')
            derrota += 1
        else:
            print('Vitória')
            vitoria += 1
    if playerGuess == 's':
        if computerGuess == 3:
            print('Empate')
            empate += 1
        elif computerGuess == 1:
            print('Derrota')
            derrota += 1
        else:
            print('Vitória')
            vitoria += 1
    time.sleep(1)
    print('-'*40)
    print('PONTUAÇÃO:')
    print("Empate(s): " + str(empate))
    print("Vitória(s): " + str(vitoria))
    print("Derrota(s): " + str(derrota))
    print('-'*40)
    i += 1
