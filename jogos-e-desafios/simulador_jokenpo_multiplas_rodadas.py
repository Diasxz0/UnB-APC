def jokenpo(rodadas):
    respostas = []
    for i in range(rodadas):
        a,b = map(str, input().split())
        if a == b:
            respostas.append("Empate.")
        elif ((a== 'tesoura' and b == "papel" or
               a == "papel" and b =="pedra" or
               a == "pedra" and b == "tesoura")):
            respostas.append("Jogador 01 venceu")
        else:
            respostas.append("Jogador 02 venceu")
    for resposta in respostas:
        print(resposta)


rodadas = int(input())
jokenpo(rodadas)