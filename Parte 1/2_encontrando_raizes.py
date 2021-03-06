# O objetivo desse código é encontramos intervalos onde o sinal do determinante é    
# invertido. Isso é um sinal de que entre esses dois valores, o determinante
# se torna zero, ou seja, uma raíz para a equacao.
# Determinar esses intervalos tornará possivel aplicar o método da bissecção
# que será executado no código 3.


# constroi a matriz Tgn a partir dos parâmetros t (matriz t x t) e l (λ)
def matI(t: int, L: int) -> list:

  m = []
  for i in range(t):
    z = []
    for j in range(t):
      if i == j:
        z.append(L)
      elif i == j + 1 or i == j -1:
        z.append(-1)
      else:
        z.append(0)
    m.append(z)
  return(m)


# implementa o método de eliminação de Gauss
# gera a matriz triangular superior
def gauss(V: list):

  sgn = 1
  for i in range(x-1):
    for j in range(x):
      if i == j and V[i][j] == 0:
        for k in range(i+1, x):
          if V[k][i] != 0:
            aux = V[k]
            V[k] = V[i]
            V[i] = aux
            sgn = sgn * (-1)**(k - i)
    if V[i+1][i] != 0:
      V[i+1] = elim(i, V)
  
  d = detV(V, sgn)

  return(d)


# faz a eliminação dos termos não nulos abaixo da diagonal principal
def elim(linha: int, A: list) -> list:

  r =  - (A[linha+1][linha] / A[linha][linha])

  linha_aux = []
  for i in range(x):
    if A[linha][i] != 0:
      linha_aux.append((A[linha][i] * r) + A[linha+1][i])
    else:
      linha_aux.append(A[linha+1][i])

  return(linha_aux)


#calcula o determinante da matriz  triangular superior gerada
# aqui há uma condicao, se a linha inteira é zero, ignoramos sua diagonal no
# calculo do determinante.
def detV(Mx: list, sinal: int) -> float:
  det = 1
  for i in range(x):
    if Mx[i][i] != 0:
      det *= Mx[i][i]
    else:
      cont = 0
      for j in range(x):
        if Mx[i][j] != 0:
          cont = 1
      if cont = 1:
        det *= Mx[i][i]

  det *= sinal

  return(det)

# retorna os intervalos onde há inversão de sinal (intervalos que contém as raízes da função)
def intervalos(g: list) -> list:

  inter = []
  for i in range(len(g)-1):
    if g[i][1] * g[i+1][1] < 0:
      linter = []
      linter.append(g[i][0])
      linter.append(g[i+1][0])
      inter.append(linter)

  return(inter)
      



#main
x = int(input())
y = (3 * x + 1)
res = []
print("         [x]          [f]\n")
for i in range(y):
  z = -2 + (i * (4/ (3 * x)))
  n = matI(x, z)
  w = gauss(n)
  vet1 = []
  vet1.append(z)
  vet1.append(w)
  res.append(vet1)
  print(f'[{i+1},] {z:.8f}, {w:.8f}')

inter = intervalos(res)
print("\nintervalos:\n")
for i in range(len(inter)):
  print(f'[{inter[i][0]:.8f}, {inter[i][1]:.8f}] ')
