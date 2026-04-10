def maiusculo(palavra):
    for letra in palavra:
        print(letra.upper(), end="")

palavra = input()
maiusculo(palavra)