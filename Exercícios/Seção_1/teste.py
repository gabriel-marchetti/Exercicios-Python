# Esse programa fala 'Oi' e pergunta sobre o meu nome:

print('Hello world!')
print('What is your name?')  # pergunta o seu nome

myname = input()

# O programa vai falar oi para você
print('It is good to meet you, ' + myname)
# O programa vai dizer o tamanho do seu nome
print('The length of your name is:')
print(len(myname))

print('What is your age?')  # pergunta a sua idade

# Salva a sua idade
myage = input()

# Diz a sua idade daqui um ano!
print('You will be ' + str(int(myage)+1) + ' in a year.')

# Input sempre retorna uma string, por conta disso é muito eficiente usarmos
