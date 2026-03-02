n = int(input("n: "))
m = int(input("m: "))

antigo = n
novo = m
resto = antigo % novo

mdc = []

while resto != 0:
    resto = antigo % novo
    antigo = novo
    novo = resto
    mdc.append(antigo)

print(mdc)
