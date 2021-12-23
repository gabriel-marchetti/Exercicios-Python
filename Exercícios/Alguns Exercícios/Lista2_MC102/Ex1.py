# Esse programa simula o comportamente de um garçom.
# Suponha que estamos em uma pizzaria com poucas opções, dito isto.
# Um programa que nos faça pedir diferentes pizzas até que nós mandamos pararem
# de mandar

print('Olá, o que a senhoria deseja de pizzinha?')

print('-'*40)
print("1 - Pizza Marguerita")
print('2 - Pizza de Calabresa')
print('3 - Pizza de Peperoni')
print('4 - Pizza de Mussarela')
print('999 - Sair')
print('-'*40)

while True:
    pedido = int(input("Qual é a escolha? "))
    if pedido == 1:
        print('Opá! Uma Marguerita saindo')
    elif pedido == 2:
        print('Essa é uma clássica! Saindo um de Calabresa')
    elif pedido == 3:
        print('O Peperoni daqui é meio ardido, então tome cuidado!')
    elif pedido == 4:
        print('Hmmmm! O queijo daqui é baum damaiss...')
    else:
        break

print('Até a próxima!')
