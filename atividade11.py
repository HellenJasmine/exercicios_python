def multiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero
    return total



resultado = multiplicacao(5,5)
print(resultado)

def is_par(a):
    return "Número é par" if a % 2 == 0 else "Número NÃO é par"

print(is_par(11))

