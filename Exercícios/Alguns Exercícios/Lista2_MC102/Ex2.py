# Faça um programa que leia um número n. Após isso, o seu programa deve ler uma
# sequência de n números e imprimir uma mensagem indicando se a sequência lida
# está ordenada de forma crescente ou não

n = int(input('Input do número: '))

i = 0
num_anterior = 0
flag = True
while i < n:
    num = int(input('Números para verificar: '))
    i += 1
    if num_anterior > num:
        flag = False
    num_anterior = num

if flag:
    print('Está em sequência')
else:
    print('Não está em sequência')
