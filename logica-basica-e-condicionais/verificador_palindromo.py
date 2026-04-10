def palindromo(palavra):
    traducao = input()
    if traducao == palavra[::-1]:
        print("Boa Deivis!")
    else: 
        print("Poxa Deivis...")

palavra= input()
palindromo(palavra)