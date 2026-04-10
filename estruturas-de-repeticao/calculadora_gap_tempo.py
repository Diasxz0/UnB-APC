def tempo_medio(n):
        tempos.extend((input().split()))
        lista_int = list(map(int,tempos))
        x = max(lista_int)
        for tempo in tempos:
                tempo = int(tempo)
                resultado = (x-tempo)
                resultados.append(resultado)
                print(resultado, end=" ")
        

n = int(input())
tempos = []
resultados = []
tempo_medio(n)
