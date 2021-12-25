# Esse programa tem a função de testar alguns comandos relacionados
# a listas. Em geral, a ideia dele é implementarmos nomes de animais
# de estimação que possuímos e no final devemos nos perguntar se
# um nome está presente na nossa lista de pets
def addPets(myPets):
    flag = True
    numPets = int(input('Quantos Pets você tem? '))
    i = 0
    while i < numPets:
        name = input('Coloque o(s) nome(s) do(s) seu(s) Pet(S): ')
        myPets.append(name)
        i += 1
    return None


def doiOwn(listOfPets, name):
    if name in listOfPets:
        print(f'Você tem um pet chamado {name}')
    elif name not in listOfPets:
        # Aqui eu poderia usar logo um else:
        # Mas eu queria deixar calara a ideia de usarmos o 'not in'
        print(f'Você não tem um pet chamado {name}')


myPets = []
addPets(myPets)
suggestName = input('Qual nome você deseja verificar? ')
doiOwn(myPets, suggestName)
