try:
    hora = int(input("Digite a hora atual: formato 24hs"))
    if 0 <= hora <= 11:
        print("Bom dia")
    if(12 <= hora <= 17):
        print("Boa tarde")
    if 18 <= hora <= 23:
        print("Boa noite")




except:
    print("usuario nao digitou um numero inteiro")