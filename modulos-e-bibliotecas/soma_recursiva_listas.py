def soma_aninhada(n):
    total = 0
    lista = []
    for numero in n:
        if isinstance(numero, list):
            total += soma_aninhada(numero)
        else:
            total += numero
    return total


print(soma_aninhada([[1,2,3]]))
