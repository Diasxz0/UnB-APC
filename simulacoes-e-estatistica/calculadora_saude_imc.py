def ComoVaiSuaSaude(p,b,h):
    IMC = p / (h * h)

    if b.lower() == "f":
        PI = (72.7 * h) - 58   
    else:
        PI = 62.1 * h - 44.7
    
    if (abs(p-PI) < 5/100*PI) and (IMC<25 and IMC>=18.5):
            return "Você tem uma saúde ótima!"
    elif (abs(p-PI) < 10/100*PI) and (IMC<25 and IMC>=18.5):
            return "Você tem uma saúde boa."
    elif (p>PI) and (IMC<18.5):
            return "Atenção: Fique atento ao baixo peso!"
    elif (abs(p-PI) > 10/100*PI) and (IMC<30 and IMC>=25):
            return "Cuidado: Medidas acima do padrão!"
    elif (abs(p-PI) > 10/100*PI) and (IMC>=30):
            return "Procure Ajuda: Excesso de medidas!"
    else: 
           return "Sem apontamento."

print(ComoVaiSuaSaude(68, "M", 1.72))
