def repeat(n):
    numeros = []
    for i in n:
        numeros.append(int(i))
    conj = set(numeros)
    if len(conj) != len(numeros):
        print("True")
    else:
        print("False")
    


n = input().split(" ")
repeat(n)
