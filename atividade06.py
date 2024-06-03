new_name =''
nome = input("Digite seu nome: ")
i = 0
while i < len(nome):
    
    new_name += f'*{nome[i]}'
    i += 1
print(new_name)

