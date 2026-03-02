import matplotlib.pyplot as plt

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

print("+"*10)
print("mdc")
print("+"*10)

print('MDC(%d,%d) = %d' % (n, m, antigo))
print(mdc)

plt.plot(mdc, '-k', linewidth=5)
plt.grid()
plt.ylabel('divisores de n e m', fontsize=16)
plt.xlabel('iterações', fontsize=16)
plt.grid()
plt.title('MÁXIMO DIVIDOR COMUM - MCD(n,m)', fontsize=16)
plt.show()
