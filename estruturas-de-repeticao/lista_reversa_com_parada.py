def reverso(n):
    numeros = list(map(int, n.split()))
    saida = []
    for numero in numeros:
        if numero>=0:
            saida.append(numero)
        else:
            break
    saida_reversa = saida[::-1]
    for item in saida_reversa:
        print(item, end=" ")

n = input()
reverso(n)