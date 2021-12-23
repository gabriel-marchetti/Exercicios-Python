# The Global Statement

# Quando quisermos modificar uma variável global
# dentro do ambiente do escopo local
# podemos fazer o seguinte comando

def spam():
    global eggs
    eggs = 'spam'


eggs = 'global'
spam()
print(eggs)
