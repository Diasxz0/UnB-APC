import math

a,b = map(int, input().split())

def co_primo(a,b):
    return math.gcd(a,b) ==1
        
if co_primo(a,b):
    print("Sao co-primos.")
else:
    print("Nao sao co-primos!")

