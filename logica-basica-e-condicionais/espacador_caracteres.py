def separar(palavra):
    palavras = palavra.split()
    for item in palavras:
        for letra in item:
            print(letra, end=" ")

palavra = input()
separar(palavra)