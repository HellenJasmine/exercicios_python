lista = ["Manteiga", "Arroz", "Feijão", "Leite","Pipoca", "Café"]
while True:
    opcao = int(input("Selecione uma opçaõ:\n 1-Inserir   2-Apagar   3-Mostrar   0-Sair\n=> "))
    while opcao not in (1,2,3,0):
        print("Digite uma opção válida!!!")
        opcao = int(input("Selecione uma opçaõ:\n 1-Inserir   2-Apagar   3-Mostrar   0-Sair\n=>"))
        if opcao in (1,2,3,0):
            break
    
    if opcao == 1:
        novo_item = input("Digite o novo item da lista => ")
        lista.append(novo_item) 
        print(lista)
        continuar = input("Deseja continuar [s]im, [n]ão  => ")
        if continuar == 'n':
            continue
    elif opcao == 2:
        indice = int(input("Digite o indice do produto que queira retirar: "))
        # if indice != enumerate(lista):
        #     print()
        #     indice = int(input("Digite o indice do produto que queira retirar: "))
        lista.pop(indice)
    elif opcao == 0:
        break
    elif opcao == 3:
        print(lista)
        for i in range(len(lista)):
            print(f"{i} - {lista[i]}")