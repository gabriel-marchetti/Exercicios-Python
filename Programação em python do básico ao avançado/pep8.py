"""
    PEP8 - Python Enhancement Proposal
    São propostas de melhorias para a linguagem Python
    
    import this
    
    A ideia do PEP8 é de padronizar os códigos Python, desse modo nosso código pode ser lido por qualquer pessoa que domine a linguagem
    
    [1] - Utilize Camel Case para nomes de classe:
        Um tópico de orientação a objetos
        
    Camel Case é um tipo de classe que será introduzido posteriormente
    
    [2] - Utilize nomes em minúsculo, separador por underline para funções ou variáveis
        # Para definir uma variável ou função, por exemplo:
        def soma():
            pass

        def soma_dois():
            pass

        numero = 4
        numero_impar = 5
    
    [3] - Utilize quatro espaços para identação!
    Podemos também utilizar a função Tab, que é muito mais rápida
    
        # Errado:
        if 'a' in 'banana':
        print('tem')
        
        # Certo:
        if 'a' in 'banana':
            print('tem')
            
    [4] - Linhas em branco
        Espaçamento entre os códigos deixa muito mais possível de ser interpretado, muito estranho isso, mas de fato acontece bastante!
        
        - Separa funções e classes com duas linhas em branco;
        - Métodos dentro de uma classe devem ser separados com uma única linha em branco;
        
        A extensão do VScode facilita bastante nesse quesito
        
    [5] - Imports:

        - Imports sempre devem ser feitos em linhas separadas;
        # Errado:
            import sys, os
        # Certo:
            import sys
            import os
            
        # Não há problema em utilizar:
            from types import StringType, ListType
            # Nesse caso estamos importanto duas classes específicas
        
        # Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:
            from type import(
                StringType,
                ListType,
                SetType,
                OutroType
            )

        #Imports devem ser colocados no topo do arquivo, literalmente no início do seu programa!! Só há algumas exceções para comentários ou docstrings
    
    [6] - Espaços em expressões ou instruções:
        # Não faça:
            funcao( algo[ 1 ], { outro: 2 } )
        # Faça:
            funcao(algo[1], {outro: 2})
            
    [7] - Termine sempre uma instrução com uma nova linha:    
"""
