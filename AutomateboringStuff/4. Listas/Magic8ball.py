# Esse programa tem como intuito migrar uma 8ball

import random

mensagens = [
    'Com certeza',
    'Sim, definitivamente',
    'Tente novamente',
    'Pergunte mais tarde',
    'Se concentre e pergunte novamente',
    'Minha resposta é não',
    'Não parece muito bom',
    'Muito duvidoso'
]

print(mensagens[random.randint(0, len(mensagens) - 1)])
