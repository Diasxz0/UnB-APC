def aprovado(n):
    for i in range(n):
        a,b,c = map(float, input().split())
        media = (a+b+c)/3
        if media>=7:
            print(f"O ALUNO {i} FOI APROVADO")
        else: 
            print (f"O ALNUO {i} FOI REPROVADO")
        
n = int(input())

print(aprovado(n))

