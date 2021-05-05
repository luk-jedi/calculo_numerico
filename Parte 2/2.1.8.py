# Por ultimo, utilizamos o método de Newton-Cotes, o mais díficil de codar 
# Obtemos o logaritmo do erro desse método e plotamos em um gráfico também.
# Dessa forma fica bem óbvia a superioridade do método de Newton-Cotes
# Quando comparado com o do Trapézio ou de Simpson.
# Mas simplesmente integrar é bem mais fácil né? Sim, então não faça cálculo
# numérico, matéria inútil e chata. Abraços.


import math
from fractions import Fraction

# realiza o método de newton da aproximação da integral
def newton(w, x, i):
  integral = 0
  ts = []
  for j in range(x+1):
    t = a + (j * ((b-a)/x))
    ts.append(t)
  
  c = 0
  for k in range(1, i+2):
    for l in range(7):
      integral += (ts[c + l]**9) * w[l]
    c += 6
  integral = integral / x
  return(integral)

# coeficientew utilizado anteriormente, com algumas alterações
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

# Lagrange utilizado anteriormente
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

#main, recebe k
a = 0
b = 1
k = int(input("k= "))
m = 10**5
w = Coeficientew(6)
for i in range(k):
  x = 6 * (i+1)
  n = newton(w, x, i)
  er = abs(0.1 - n)
  # print(n) usado apenas para testes
  print(math.log(er))