x = round(5.76543, 2)
print(x)
# Aproxima o valor para duas casas decimais

p = round(9, 2)
print(p)
# Não transforma em float

p_2 = round(9.000, 2)
print(p)
print(type(p_2))
# Ele retorna como float na verdade kkkkk

# a syntax dele se resume a round(number, digits)

p_3 = round(9000, 3)
print(p_3)
# só atrapalha numeros depois da vírgula

# abs é uma função bem clara, ela retorna o valor absoluto do argumento
print(abs(-2))
