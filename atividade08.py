import os

palavra_secreta = "morango"
letras_acertadas  = ""
while True:

    try:
        letra = input("Tente adivinhar a palavra\nDigite 1 letra: ")
        if len(letra) > 1:
            print("Erro, digite apenas 1 letra")
            letra = input("Digite uma letra")
    except:
        print("erro ")
        break
    if letra == "0":
        break

    if letra in palavra_secreta:
        letras_acertadas += letra


    palavra_formada = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada +="*"
    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system("cls")
        print("Você ganhou")