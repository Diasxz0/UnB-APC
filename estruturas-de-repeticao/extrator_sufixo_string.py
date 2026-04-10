def is_in(entrada):
    partes = entrada.split()
    a = partes[0]
    b = int(partes[1])
    len_a = len(a)
    contador = len_a - b -1
    print(a[contador:])



entrada = input()
is_in(entrada)