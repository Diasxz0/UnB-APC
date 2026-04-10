def prefix(n):
    lista = list(map(int, n.split()))
    soma= 0
    for item in lista:
        soma+=item
        print(soma, end=" ")  
    print()  
    for numero in lista:
        print(f"{numero}", end=" ")

n = input()
prefix(n)
