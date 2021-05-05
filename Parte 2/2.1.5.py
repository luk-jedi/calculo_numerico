# A seguir, utilizamos a fórmula para somar termos infinitos de uma
# progressão geométrica, a fim de descobrir quais as frações que dão 
# origem as dízimas periódicas calculadas anteriormente.


import math
from fractions import Fraction

# Calcula os coeficientes w, pelo método de Simpson.
def Coeficientew (n):
  ws = []
  h = (b - a)/n
  for i in range(m+1):
    t = a + i *((b-a)/m)
    f = Lagrange(n, t)
    for j in range(len(f)):
      if i == 0:
        ws.append(f[j])
      elif i == m:
        ws[j] += f[j]
      elif i % 2 == 0:
        ws[j] += 2 * f[j]
      else:
        ws[j] += 4 * f[j]
  for i in range(len(ws)):
    ws[i] = (((b-a)/(3 * m)) * ws[i])/h
  return(ws)

# calcula os polinomios de lagrange 
def Lagrange (n, t):
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
                li = li*(t - xn[j])/(xn[i] - xn[j])
        ln.append(li)
    return(ln)

# recebe os valores de w e obtém as frações que deram origem a eles
def fractionS(g):
  sn = []
  for i in range(len(g)):
    soma = round(g[i], 2) + (285714/10**8) * ((10**6)/(10**6 - 1))
    sn.append(Fraction(soma).limit_denominator())
  return(sn)

a = 0
b = 1
m = 10**5
x = int(input("n = "))
g = (Coeficientew(x))
print(fractionS(g))