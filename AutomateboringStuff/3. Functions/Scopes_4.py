# Esse programa tem como intuito mostrar que:
# variáveis de escopo global podem ser lidas dentro
# de escopos locais:

# Por exemplo vamos fazer que

def spam():
    # eggs = 10
    # veja que se redefinirmos essa variável nesse escopo
    # ele da prioridade para o escopo local
    # em vez de atribuir o valor da variável para o
    # escopo global
    print(eggs)


eggs = 42
spam()
print(eggs)
