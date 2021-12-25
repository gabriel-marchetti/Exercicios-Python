# A biblioteca random possui algumas aplicações para listas!

import random

# Suponha uma lista:
pessoas = ['Gabriel', 'Karyn', 'Higor', 'Akay']

# o comando random.shuffle
random.shuffle(pessoas)
print(pessoas)

x = random.choice(pessoas)
print(x)
