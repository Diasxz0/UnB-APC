def americano(palavra):
    resposta = []
    for letra in palavra:
        if ((letra.lower() == "a" or 
             letra.lower() == "e" or 
             letra.lower() == "i" or
             letra.lower() == "o" or
             letra.lower() == "u" or
             letra.lower() =="y")):
            continue
        else:
            resposta.append("."+letra.lower())
    print("".join(resposta))
            

palavra = input()
americano(palavra)