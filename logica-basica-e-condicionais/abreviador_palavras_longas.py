def abreviacao(numero):
    respostas = []
    for i in range(numero):
        palavra = input()
        if len(palavra)<=10:
            respostas.append(palavra)
        else:
            respostas.append(f"{palavra[0]}"+f"{len(palavra)-2}"+f"{palavra[len(palavra)-1]}")

    for resposta in respostas:
        print(resposta)

numero = int(input())
abreviacao(numero)