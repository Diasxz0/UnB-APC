def inverter_numero_reversed(numero):
    if numero>=0:
        return int("".join(reversed(str(numero))))
    else: 
        return "-" + str("".join(reversed(str(numero*-1))))

numero = int(input())

print(inverter_numero_reversed(numero))
