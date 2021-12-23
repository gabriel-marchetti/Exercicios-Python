# Esse programa tem o intuito de visualizarmos
# os escopos das variáveis
# Sabemos que uma variável de um escopo local não
# pode ser usada em um escopo global
# Portanto, consideremos o seguinte programa

def spam():
    eggs = 31337


spam()
print(eggs)

# Veja que esse programa necessariamente vai dar um erro
# visto que o escopo de 'eggs' está dentro da função spam
# portanto, o vscode está totalmente certo em mostrar um erro
# nesse caso :)

# Isso pode ser visto principalmente pela mensagem de erro
# que é "name 'eggs' is not defined", pois justamente essa
# variável está restrita ao escopo 'spam' 

