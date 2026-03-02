import math as m


a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

delta = b**2-4*a*c


if delta > 0:

    x1 = (-b+m.sqrt(delta))/(2*a)
    x2 = (-b-m.sqrt(delta))/(2*a)

    print(f'x1 = {x1}')
    print(f'x2 = {x2}')
elif delta == 0:
    x1 = b/(2*a)
    print(f'As duas raízes reais e iguais - x1 = {x1}')

else:
    print("Não existem raízes reais")
