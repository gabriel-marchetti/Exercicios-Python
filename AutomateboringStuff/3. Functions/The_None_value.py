# Esse programa tem como função testar um fato que muitas
# passa despercebido em um programa.
# Nesse caso testaremos a função de retorno das funções!
# Primeiro temos que atentar que toda função do python
# possui algum retorno.
# Nesse caso teremos que o print() possui retorno, assim
# como qualquer outra função como len(), por exemplo.

# Dado isso, vamos testar o seguinte programa

Spam = len('Hello')
print(Spam)

# No terminal devemos ter uma função que retorna 5
# Portanto, fazendo um teste do tipo
print(Spam == None)

# Deve nos retornar um valor falso!

# Agora, vamos fazer o teste para a função print()
Ham = print('Hello')

# Isso deve nos imprimir no terminal 'Hello':
# Agora vejamos que:
print(Ham == None)

# Deve nos retornar o valor True!

# Isso ocorre porque como vimos, o retorno da
# função print não é escrever no terminal
# isso é um processo dentro da própria função
# e como toda função retorna algum valor
# o valor de retorno da função print()
# é None.
