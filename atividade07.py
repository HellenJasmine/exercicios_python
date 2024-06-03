while True:
    operadores = ("+","-","/","*")
    try:
        num1 = float(input("Digite um número:"))
        num2 = float(input("Digite um outro número"))
        operador = input("Qual operação deseja realizar? (+, -, /, *)")
        while operador not in operadores:
            if len(operador) > 1:
                print("Digite apenas 1 operador!!!")
            operador = input("Operador inválido!!!\nDigite um operador válido:\n(+, -, /, *)")
    except:
        print("Você não digitou um número")
        break

    if operador == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operador == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operador == "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    else:
        print(f"{num1} / {num2} = {num1 / num2}")

