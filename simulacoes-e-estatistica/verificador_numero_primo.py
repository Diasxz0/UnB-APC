import math

def primo(n):
    if n<=1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limite = int(math.sqrt(n))+1
    for i in range (3,limite, 2):
        if n%i == 0:
            return False
    return True
        
    
    


n = int(input())

if primo(n):
    print("primo")
else:
    print("regular")