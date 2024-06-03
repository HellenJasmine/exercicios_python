try:
    nome = input("Digite seu PRIMEIRO NOME: ")
    if len(nome) <= 4 :
        print("Nome Curto")
    elif len(nome) == 5 or len(nome) == 6 :
        print("Nome tamanho normal")
    else:
        print("Nome muito grande")


except:
    print("Você nao digitou um numero")