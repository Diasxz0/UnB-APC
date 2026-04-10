def susbtituicao(palavra):
    a = palavra.replace("e", "a").replace("i", "a").replace("o", "a").replace("u", "a")
    print(a)
    b = palavra.replace("a", "e").replace("i", "e").replace("o", "e").replace("u", "e")
    print(b)
    c = palavra.replace("e", "i").replace("a", "i").replace("o", "i").replace("u", "i")
    print(c)
    d = palavra.replace("e", "o").replace("i", "o").replace("a", "o").replace("u", "o")
    print(d)
    e = palavra.replace("e", "u").replace("i", "u").replace("o", "u").replace("a", "u")

palavra = input()
susbtituicao(palavra)

