# No segundo exercício, calculamos os coeficientes w através
# do método dos trapézios, esses coeficientes são necessários para realizar 
# a aproximação de Newton-Cotes. A precisão desses coeficientes depende do 
# valor de partições que o intervalo a ser integrado foi dividido.
# Aqui utilizamos 10^5, que já gera uma precisão razoável.


import math

# recebe n e utiliza os polinômios gerados pela função lagrange para calcular
# os coeficientes w.
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
      else:
        ws[j] += 2 * f[j]
  for i in range(len(ws)):
    ws[i] = (((b-a)/(2 * m)) * ws[i])/h
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