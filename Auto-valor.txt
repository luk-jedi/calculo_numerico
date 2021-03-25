# Esse código realiza a eliminação de Gauss de uma matriz Tg da Teoria dos Grafos.
# O usuário deve inserir dois valores, o primeiro é o tamanho da matriz, o segundo refere-se
# ao valor de lambda que será atribuido na diagonal principal.
# A matriz trabalhada é composta por uma diagonal principal com valores lambda, os valores ao redor
# da diagonal principal são -1, e os restantes são 0.
# após a eliminação de todos os valores diferentes de 0 das posições abaixo da diagonal,
# o programa realiza o cálculo do Determinante (que é obtido multiplicando os valores da diagonal 
# principal vezes um fator de sinal que depende da troca ou não de linhas na matriz.
# Esse tipo de matriz é muito importante, utilizado até mesmo por algoritmos do Google, como segue
# no link abaixo:
# https://www.math.arizona.edu/~glickenstein/math443f08/bryanleise.pdf

# imprime na tela a matriz (t x t) com λ = l, escolhidos pelo usuário
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
  for i in range(t):
    for j in range(t):
      print(f"{m[i][j]:^3}", end=" ")
    print("\n")
  return(m)


# implementa o método de eliminação de Gauss
# imprime a matriz triangular superior
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
  
  print("\n\n\nV_linha\n")
  for i in range(x):
    for j in range(x):
      print(f"{V[i][j]:^8.4f}", end=" ")
    print("\n")

  print(f"\n\n\n>Determinante\n\n{detV(V, sgn)}")

  return()


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



#main
x = int(input())
y = int(input())
print("\n\n\n>V\n")
n = matI(x, y)
gauss(n)