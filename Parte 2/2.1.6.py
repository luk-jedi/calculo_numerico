# Você por acaso achou que tava chato achar esses valores de w?
# Pois existe um método mais chato ainda, fazer uma multiplicação de matrizes!
# para isso montamos uma matriz quadrada com as partições elevadas a k
# multiplicamos pelas icógnitas w, e igualamos a uma matriz com valores
# (n / k + 1). Esse k no caso, é a linha da matriz.
# Realizamos a eliminação de Gauss e na sequencia resolvemos o sistema linear.


import math
from fractions import Fraction
import numpy as np

# realiza a eliminação de Gauss da matriz
def gauss(A):
    n = len(A)
    for i in range(0, n):
      for k in range(i + 1, n):
        c = -A[k][i] / A[i][i]
        for j in range(i, n+1):
          if i == j:
            A[k][j] = 0
          else:
            A[k][j] += c * A[i][j]
    acha_w(A)

# calcula os polinomios de lagrange 
def Lagrange (n):
  xn = []
  for i in range(n+1):
    h = (b - a)/n
    xi = a + i*h
    xn.append(xi)
  eleva(n, xn)

# monta a matriz elevando as partições a "k"
def eleva(n, xn):
  mat = []
  for i in range(n+1):
    linha = []
    for j in range(n+2):
      if j < n+1:
        linha.append(xn[j]**i)
      else:
        linha.append(n/(i+1))
    mat.append(linha)
  gauss(mat)

# resolve o sistema linear e encontra os valores de w.
def acha_w(mg):
  res = []
  for i in range(x+1):
    res.append(mg[i][x+1])
    del mg[i][x+1]

  B = np.array(mg)
  C = np.array(res)
  D = np.linalg.inv(B).dot(C)
  print(D)

# main. Recebe o valor de n
a = 0
b = 1
m = 10**5
x = int(input("n = "))
Lagrange(x)