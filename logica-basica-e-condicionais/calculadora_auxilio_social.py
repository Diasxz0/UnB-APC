pessoas = int(input())

grana = []
valor = 0

for i in range(pessoas):
    grana.append(int(input()))
    if grana[i]<1000:
        valor = valor + (1000 - grana[i])
    else:
        valor = valor
print(valor)
        
