# Suponha que desejamos simular uma aplicação CallStack
# Então, seja um programa do tipo
def main():
    a()


def a():
    print('a() starts')
    b()
    d()
    print('a() returns')


def b():
    print('b() starts')
    c()
    print('b() return')


def c():
    print('c() starts')
    print('c() returns')


def d():
    print('d() starts')
    print('d() returns')


main()

# Veja que o análogo da conversa pode ser feito,
# vamos substituir as letras por nomes
# seja A: Alice, então temos que a primeira conversa
# sobre a Alice termina apenas na última linha
# Enquanto que B: Bob imediatamente começa e logo depois
# entramos no assunto sobre C: Charlie e assim por diante

# Isso praticamente descreve uma "arvore" de CallStack
# pois todas as vezes que chamamos uma nova função
# ela nos retorna a partir do ponto em que paramos
