# Como foi dito anteriormente, a precisão dos valores de w sempre depende
# do número de divisões do intervalo. Entretanto, 10^5 já é um valor que
# a maioria dos computadores leva um tempinho pensando. Aumentar para 10^6
# ou 10^7 seria um processo improdutivo, por isso vale mais utilizar um método
# que consiga precisões melhores, como o Método de Simpson, implementado abaixo.


import math
from fractions import Fraction

# Calcula os coeficientes w, desta vez pelo método de Simpson.
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

# main. Deve ser inserido o valor de n
a = 0
b = 1
m = 10**5
x = int(input("n = "))
print(Coeficientew(x))