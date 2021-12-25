# Esse programa tem como intuito verificar os usos da função
# enumerate do python

flag = True
diasDeFeriado = []
while flag:
    dia = input('Qual dia tem feriado? ')
    if dia.lower() == 'pare':
        break
    diasDeFeriado.append(dia)

mes = int(input('Qual mês esses feriados vão acontecer? '))

for index, item in enumerate(diasDeFeriado):
    print(f'o {index+1}° feriado é dia {item}/{mes}')
