def remove_duplicatas(n):
    lista_sem_duplicata = []
    for numero in n:
        if numero not in lista_sem_duplicata:
            lista_sem_duplicata.append(numero)
    return lista_sem_duplicata

