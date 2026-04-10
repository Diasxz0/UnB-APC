numeros = []
rep=0

while True:
    a = int(input())
    if a != -1:
        numeros.append(a)
        rep+=1
    else:
        break

numerador = len(numeros)

denominador = 0
for numero in numeros:
    denominador = denominador + 1/numero

resultado = numerador//denominador

print(int(resultado))
    