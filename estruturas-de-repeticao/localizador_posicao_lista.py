def ordena(n):
    lista = list(map(int, input().split()))
    lista.append(n)
    lista = sorted(lista)
    if n == max(set(lista)) and len(set(lista)) == 1:
        print("0")
    elif n != max(set(lista)):
        print(lista.index(n))
    else:
        print("-1")


    


n = int(input())
ordena(n)