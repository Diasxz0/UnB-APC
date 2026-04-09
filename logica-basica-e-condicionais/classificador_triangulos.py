def classificador(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        print("triangulo")
        if a!=b and b!=c and c!=a:
            print("escaleno")
            if a**2 == b**2 + c**2 or c**2 == b**2 + a**2 or b**2 == a**2 + c**2:
                print("retangulo")
        elif a==b or b==a or c==a:
            print("isosceles")
            if a==b and b==c:
                print("equilatero")
    else:
        print("gondim sendo gondim")

classificador(3, 5, 4)
classificador(2, 1, 1)
classificador(3, 3, 3)