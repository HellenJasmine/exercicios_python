try:
    number = int(input("Digite um número inteiro: "))
    number_is_par = "par" if number%2==0 else "impar"
    if number% 2 == 0:
        print(f"{number} é {number_is_par}")
    else:
        print(f"{number} é {number_is_par}")
except:
    print("Usuário nao informou numero inteiro")


