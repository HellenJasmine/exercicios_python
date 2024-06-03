
import random

cpf = ""
for i in range(9):
    cpf += str(random.randint(0,9))

print(cpf)

soma_digito1 = 0
contador_regressivo_1 = 10

for numero in cpf:
    soma_digito1 += contador_regressivo_1 * int(numero) 
    contador_regressivo_1 -=1


digito_1 = (soma_digito1 *10) % 11 
digito_1 = digito_1 if digito_1 <= 9 else 0

contador_regressivo_2 = 11
cpf = cpf + str(digito_1)
soma_digito2 = 0
for numero in cpf:
    soma_digito2 += contador_regressivo_2 * int(numero)
    contador_regressivo_2 -= 1
digito_2 = (soma_digito2 * 10) % 11
digito_2 = digito_2 if digito_2 <=9 else 0

cpf_gerado = f"{cpf}{digito_2}"
print(cpf_gerado)
