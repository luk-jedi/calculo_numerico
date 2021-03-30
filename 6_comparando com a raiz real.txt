# Neste ultimo exercicio, comparamos a eficácia dos nossos métodos de aproximação de raíz
# com a raíz real. Através de alguns postulados matemáticos, sabemos que a raíz exata desse
# determinante pode ser obtida por "-2 * cos((i * pi)/12)". Dessa forma, utilizamos o 
# método de newton, mas partindo da raíz aproximada calculada pelo método da bissecção
# e tentamos atingir a raíz exata com o maior precisão possível (aqui utilizaremos 12).
# É possivel perceber que a junção dos dois métodos atinge o valor da raíz de forma
# satisfatória. 





import math

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
def detV(Mx: list, sinal: int) -> float:
  det = 1
  for i in range(x):
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
      

#utiliza o metodo da bisseccao para diminuir cada vez mais os intervalos,
# até encontrar a raiz com precisão 10^-5.
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


# calcula a derivada da função f
# recebe como parâmetro o tamanho da matriz e o λ
def derivada (tam: int, lam: float):
  z = lam / 2

  if lam == 2:
    d1 = (tam + 1)**5
    d2 = (tam + 1)**3
    d = (d1 - d2) / 3
  elif lam == -2:
    d1 = (tam + 1)**5
    d2 = (tam + 1)**3
    d = ((-1)**(tam+1)) * ((d1 - d2) / 3)
  else:
    d1 = (tam+1)*math.cos((tam+1)*math.acos(z))
    d2 = z*((math.sin((tam+1)*math.acos(z)))/(math.sin(math.acos(z))))
    d = (d1 - d2)/(2*((z**2)-1))
  return(d)


# uma função que condensa a função matI e a função gauss para um
# dado valor, para facilitar as funções que precisam do 
# determinante de um dado valor.
def simples(s: float) -> float:
  t = matI(x, s)
  u = gauss(t)
  return(u)     


# função que calcula a raíz do determinante utilizando o metodo
# de newton. ela recebe uma lista com todos os valores de 
# intervalos onde foi identificado que ocorre a inversão de sinais.
# recebe uma lista com as aproximacoes da funcao bisseccao e a paritr 
# dessa aproximação encontra as raízes aproximadas pelo metodo de newton
def newton(f: list, g: list) -> list:
  news = []
  for i in range(len(f)):
    c = 0
    e = 10**(-12)
    a = f[i][0]
    b = f[i][1]
    alfa = g[i]

    while simples(alfa + e) * simples(alfa - e) > 0 and c <= 100:
      c += 1
      if alfa >= a and alfa <= b:
        alfa = alfa - (simples(alfa)/ derivada(x, alfa))
    news.append(alfa)
  return(news)  


#calcula as raízes a partir da formula dada
def raizcos(r: int) -> list:
  lcos = []
  for i in range(1, r+1):
    rai = -2 * math.cos((i * math.pi)/12)
    lcos.append(rai)
  return(lcos)



#main
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

nw = newton(inter, rot)
print(f"raiz newton: \n{nw}\n")

rc = raizcos(x)
print(f"raiz cos: \n{rc}\n")

sub = []
for i in range(x):
  su = abs(nw[i] - rc[i])
  sub.append(su)
print(f"erros: \n{sub}")