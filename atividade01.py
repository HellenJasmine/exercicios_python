

name = input("Digite seu nome: ou  para sair")
age = input("Digite sua idade: ")


if name and age != '':
    print(f"Seu nome é {name}")
    print(f"Seu nome invertido é {name[::-1]}")
    print(f"Seu nome contém ou não {" " in name} espaços")
    print(f"Seu nome tem {len(name)} letras")
    print(f"A letra do seu primeiro nome é {name[0]}")
    print(f"A última letra do seu nome é {name[-1]}")
else:
    print("nao digitou nada")