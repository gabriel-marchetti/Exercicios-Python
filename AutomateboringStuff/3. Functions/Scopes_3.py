# Esse programa tem como intuito mostrar casos
# em que escopos locais não podem ser usadas
# dentro de escopos de outras variáveis locais

# Segue o programa:

def spam():
    eggs = 99
    bacon()
    print(eggs)


def bacon():
    ham = 101
    eggs = 0


spam()

# Como podemos ver, quando o programa se inicia, chamamos a função
# spam, nesse ato de chamarmos essa função criamos um escopo local
# por consequência da função 'spam' chamar outra função chamada
# 'bacon', então criamos outro escopo dentro da função
# que por coincidência tem uma variável 'eggs'
# como terminamos de executar a variável 'eggs' dentro do escopo
# da função 'bacon', então lembremos do exemplo de um container
# sendo jogado for, de modo que as variáveis dentro do container
# também são esquecidas, desse modo, as variáves restantes
# são as que estão dentro do escopo 'spam' novamente. Por conta disso
# o resultado final do nosso programa é a variável 'eggs' dentro do
# escopo de spam()
