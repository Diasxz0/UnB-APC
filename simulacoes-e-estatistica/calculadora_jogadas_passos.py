def jogadas(a,b):
    if a==b:
        print("0")
    elif a<b:
        if (((b-a) % 10) % 10) !=0:
            print((b-a) //10 +1)
        else:
            print((b-a)//10)  
    else:
        if (((a-b) // 10) % 10) !=0:
            print((a-b) // 10 + 1)
        else:
            print((a-b) // 10)  


jogadas(5, 5)
jogadas(13, 42)
jogadas(18, 4)	
jogadas(1337, 420)
jogadas(1234, 10000)
jogadas(100500, 9000)
jogadas(1000,1101)


