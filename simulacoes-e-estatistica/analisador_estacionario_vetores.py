def vetor(n):
    primeiro = []
    segundo = []
    terceiro = []
    for i in range(n):
        a,b,c = map(int, input().split())
        primeiro.append(a)
        segundo.append(b)
        terceiro.append(c)
    if ((sum(primeiro) == 0 and
         sum(segundo) == 0 and
         sum(terceiro) == 0)):
        print("ESTACIONARIO")
    else:
        print("MOVIMENTO")
    print(primeiro)
    print(segundo)
    print(terceiro)
n = int(input())
vetor(n)