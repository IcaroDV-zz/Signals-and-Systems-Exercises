#Try it in jupyter notebook

def f(x):
    return 2*x**2 - x + 4
x = float(input("Digite o valor de x: "))

print(f(x))

import sympy as sp

x = sp.Symbol('x')
y = 2*x**2 - x + 4
sp.plot(y)