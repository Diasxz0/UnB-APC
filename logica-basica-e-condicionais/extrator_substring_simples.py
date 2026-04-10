def substring(palavra):
    respostas = []
    for numero in range(palavra):
        a,b,c = map(str, input().split())
        a = int(a)
        b = int(b)
        respostas.append(c[a:b+1])
    for resposta in respostas:
        print(resposta)
        

        

palavra = int(input())
substring(palavra)