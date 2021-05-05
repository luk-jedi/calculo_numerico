# Nesta segunda parte iremos explorar alguns métodos de aproximar integrais.
# Os métodos utilizados são o dos trapézios, o de Simpson e de Newton-Cotes.
# Neste primeiro exercício é demonstrada a aplicação do polinômio de Lagrange,
# utilizado para a realização dessas aproximações.

import math

# calcula os polinomios de lagrange
def Lagrange (n: int, x):
    xn = []
    ln = []
    for i in range(n+1):
    
        h = (b - a)/n
        xi = a + i*h
        xn.append(xi)

    for i in range(n+1):
        li = 1
        for j in range(n+1):
            if i != j:
                li = li*(x - xn[j])/(xn[i] - xn[j])
        ln.append(li)
    print("\n")
    return(ln)

# main. Deve-se inserir n e escolher o ponto a ser utilizado
a = 0
b = 1
m = int(input("n = "))
xis = int(input("\n\n[1] x = pi/6\n[2] x = 2\n\nchoose x: "))

if xis == 1:
    print(Lagrange(m, math.pi/6))
else:
    print(Lagrange(m, 2))