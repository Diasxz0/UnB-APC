code = float(input())
lseq = float(input())
P1 = float(input())
ldec = float(input())
P2 = float(input())
lrep = float(input())
P3 = float(input())

Nseq = (0.1*code) + (0.2*lseq) + (0.7*P1)
Ndec = (0.2*ldec) + (0.8*P2)
Nrep = (0.1*lrep) + (0.9*P3)

MF = (Nseq + 2*Ndec + 3*Nrep)/6
print(MF)


if MF >= 5:
  print("Aprovado")
else:
  print("Reprovado")