# fibonacci

n = int(input("Número de termos desejado: "))

ult = 0
penul = 1
i = 3

while i <= n:
    soma = ult+penul
    print(f"termo: {i}, fibonacci: {soma}")
    ult = penul
    penul = soma
    i += 1
