def tamanho(palavra):
    contador = 0
    for i in palavra:
        contador +=1
    print(contador)

palavra = input()
tamanho(palavra)