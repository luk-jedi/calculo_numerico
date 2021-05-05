# Agora chegou a hora da verdade, verificar qual dos métodos de aproximação é melhor.
# Para isso, testamos os métodos do trapézio e de Simpson para uma mesma função (x^9)
# Vamos alterando o valor de m, ou seja, aumentando progressivamente o número de 
# divisões do intervalo, e observamos qual dos métodos se aproxima mais rapidamente
# do valor correto. Para isso, utilizamos o logaritmo do erro para construir um gráfico
# através do metodo dos mínimos quadrados, observamos qual gráfico tem um coeficiente 
# linear menor. Este será o que se aproxima mais rápido do valor correto.


import math

# calcula a integral pelo método dos trapezios
def trapezio (n):
  integral = 0
  h = (b - a)/n
  for i in range(n+1):
    t = a + i *((b-a)/n)
    if i == 0 or i == n:
      integral += t**9
    else:
      integral += 2 * (t**9)
  integral = (h * integral) / 2 
  
  return(integral)

# calcula a integral pelo método de Simpson
def simpson (n):
  integral = 0
  h = (b - a)/n
  for i in range(n+1):
    t = a + i *((b-a)/n)
    if i == 0 or i == n:
      integral += t**9
    elif i % 2 == 0:
      integral += 2 * (t**9)
    else:
      integral += 4 * (t**9)
  integral = ((b-a) * integral) / (3*n)
  return(integral)

# main. recebe o valor de m
a = 0
b = 1
x = int(input("m = "))
for i in range(10): 
  y = x * (i+1)
  t = trapezio(y)
  s = simpson(y)
  erro_t = abs(0.1 - t)
  log_t = math.log(erro_t)
  erro_s = abs(0.1 - s)
  log_s = math.log(erro_s)

  log_m = math.log(y)

  print(f"para m = {y}")
  print(f"log m = {log_m} \nlog ET= {log_t}")
  print(f"log ES = {log_s}\n")