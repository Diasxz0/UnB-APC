numeros = []
rep=0
media = 0
while True:
    a = int(input())
    if a != -1:
        numeros.append(a)
        rep+=1
    else:
        break

for numero in numeros:
    media = media + numero
print(media)
print(f"{(media//rep)}")