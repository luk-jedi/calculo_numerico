# seguindo os estudos nos codigos anteriores, nesse aqui iremos realizar uma aproximação para a derivada
# dos numeros obtidos no exercicio anterior. Essa raiz será utilizada para fazer o método de Newton no 
# codigo seguinte.




import math

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
    print(d)

#main
x = int(input())
y = float(input())
derivada(x, y)