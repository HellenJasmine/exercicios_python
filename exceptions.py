number_str = input("Digite um numero para eu mostrar o dobro: ")

try:
    number_float = float(number_str)

    print(f"O dobro de {number_str} é {number_float * 2:.2f}")
except:
    print("Isso não é um número")