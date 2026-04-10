def substring(palavras):
    contador = -1
    respostas = []
    for numero in range(palavras):
        a,b,c = map(str, input().split())
        a = int(a)
        b = int(b)
        for letra in c:
            contador+=1
        reverso = reversed(c)
        reverso = list(reverso)
        index_inicio = contador - b   
        index_final = contador - a+1
        contador = -1 
        reverso = "".join(reverso)
        respostas.append(str(reverso[index_inicio:index_final]))
    
    for resposta in respostas:
        print(resposta)

palavras = int(input())
substring(palavras)