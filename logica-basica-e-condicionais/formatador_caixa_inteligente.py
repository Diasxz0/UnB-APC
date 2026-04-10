def letter(palavra):
    maiuscula = []
    minuscula = []
    for letra in palavra:
        if letra == letra.upper():
            maiuscula.append(letra)
        else:
            minuscula.append(letra)
    if len(maiuscula) > len(minuscula):
        print(palavra.upper())
    else:
        print(palavra.lower())


palavra = input()
letter(palavra)