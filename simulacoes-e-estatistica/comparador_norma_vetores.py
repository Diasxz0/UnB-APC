def maior_norma(a, b):
    L1 = []
    L2 = []
    for item in a:
        L1.append(abs(item))
    for numero in b:
        L2.append(abs(item))
    if sum(L1)>sum(L2):
        print("PRIMEIRO")
    else:
        print("SEGUNDO")
