# no codigo dois os intervalos one o determinante se inverte foram encontrados.
# Agora, aplicamos o método da bissecção, que consiste em basicamente encontrar
# o valor central do intervalo [a,b], calcular o determinante e observar se a raíz
# ficou entre o 'a' e o valor central, ou entre o valor central e 'b', fechando o 
# intervalo. Repetimos o processo até a precisão 10^-5.


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


def elim(linha: int, A: list) -> list:

  r =  - (A[linha+1][linha] / A[linha][linha])

  linha_aux = []
  for i in range(x):
    if A[linha][i] != 0:
      linha_aux.append((A[linha][i] * r) + A[linha+1][i])
    else:
      linha_aux.append(A[linha+1][i])

  return(linha_aux)

def detV(Mx: list, sinal: int) -> float:
  det = 1
  for i in range(x):
    if Mx[i][i] != 0:
      det *= Mx[i][i]

  det *= sinal

  return(det)


def intervalos(g: list) -> list:

  inter = []
  for i in range(len(g)-1):
    if g[i][1] * g[i+1][1] < 0:
      linter = []
      linter.append(g[i][0])
      linter.append(g[i+1][0])
      inter.append(linter)

  return(inter)
      

def bisseccao(ints: list):
  roots = []
  for i in range(len(ints)):
    a = ints[i][0]
    b = ints[i][1]
    c = 0
    cont = 0
    while cont == 0:
      c = (a + b) /2
      n1 = matI(x, c)
      w1 = gauss(n1)
      n2 = matI(x, a)
      w2 = gauss(n2)

      nmais = matI(x, c + 10**(-5))
      wmais = gauss(nmais)
      nmenos = matI(x, c - 10**(-5))
      wmenos = gauss(nmenos)

      if wmais * wmenos < 0:
        cont = 1
      elif w2 * w1 < 0:
        b = c
      else:
        a = c
    
    roots.append(c)

  return(roots)

       



x = int(input())
y = (3 * x + 1)
res = []

for i in range(y):
  z = -2 + (i * (4/ (3 * x)))
  n = matI(x, z)
  w = gauss(n)
  vet1 = []
  vet1.append(z)
  vet1.append(w)
  res.append(vet1)

inter = intervalos(res)

rot = bisseccao(inter)
print("roots:\n")
for i in range(len(rot)):
  print(f'{rot[i]:.7f}', end = ",\n")