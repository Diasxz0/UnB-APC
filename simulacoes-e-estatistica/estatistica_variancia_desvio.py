import math
def var(n):
    valores = list(map(float, n.split()))
    media = sum(valores)/ len(valores)
    result = 0
    for valor in valores:
        resultado = (valor-media)**2
        result +=resultado 
    fim = result/len(valores)
    print(f"{fim:.1f}")
    print(f"{math.sqrt(fim):.1f}")
    

n = str(input())
var(n)
