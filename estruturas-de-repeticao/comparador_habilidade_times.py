def habilidade(numero):
    niveis = str(input())
    nievis_list = list(map(int, niveis.split()))
    nievis_list = sorted(nievis_list)
    nievis_list = reversed(nievis_list)
    nievis_list = list(map(int, nievis_list))
    titulares = nievis_list[0:11]
    reservas = nievis_list[11:22]
    print(sum(titulares) - sum(reservas))

numero = int(input())
habilidade(numero)
