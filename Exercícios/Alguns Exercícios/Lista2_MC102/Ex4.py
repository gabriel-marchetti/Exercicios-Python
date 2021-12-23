# Escreva um programa que leia um número n. O seu programa deve imprimir o
# menor número primo que é maior ou igual n e o maior número primo que é menor
# ou igual a n.

# Funções:
# verif_primo:
# Verifica se um número é primo
# Entradas:
#   num: número a ser verificado
# Saídas
#   prim_menor: número primo menor ou igual a num
#   prim_maior: número primo maior ou igual a num
import time  # Isso aqui eu usei para testar um tempo


def verif_primo_maior(num):
    spark_1 = num
    while True:
        lista_divisores_1 = []
        # Maior primo
        for divisor in range(1, spark_1+1):
            if spark_1 % divisor == 0:
                lista_divisores_1.append(divisor)
        if len(lista_divisores_1) <= 2:
            return lista_divisores_1
        spark_1 += 1


def verif_primo_menor(num):
    spark_1 = num
    while True:
        lista_divisores_1 = []
        # Menor primo
        for divisor in range(1, spark_1+1):
            if spark_1 % divisor == 0:
                lista_divisores_1.append(divisor)
        if len(lista_divisores_1) <= 2:
            return lista_divisores_1
        spark_1 -= 1


# Input do número
num = int(input('Qual o número a ser verificado? '))

maior = verif_primo_maior(num)[-1]
menor = verif_primo_menor(num)[-1]

if menor == maior:
    print('O número é primo e seu número é: ' + str(menor))
else:
    print('O maior primo é: ' + str(maior))
    print('O menor primo é: ' + str(menor))
