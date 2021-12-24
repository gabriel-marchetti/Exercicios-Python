# Esse programa tem como intuito fazer um desenho de zigzag no terminal

# Vamos importar as bibliotecas
import time
import sys

indent = 0  # Isso irá nos dizer quantos espaços haverão à frente
indentIncreasing = True  # Dirá se a identação está aumentando
# ou diminuindo

try:
    while True:  # Começaremos o loop do programa
        print(' '*indent, end='')  # Irá dispor o número de espaços
        print('*******')  # O indicador do ZigZag
        time.sleep(0.1)  # Pausar o programa para visualizamos o ZigZag

        if indentIncreasing:
            # Aumenta o número de espaços:
            indent += 1
            if indent == 20:
                # Diminui o número de espaços
                indentIncreasing = False
        else:
            # Diminui o número de espaços:
            indent -= 1
            if indent == 0:
                # Muda direção
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
