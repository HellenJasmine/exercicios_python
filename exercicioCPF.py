import re
import sys
import random

cpf = "614.294.943-01"
cpf
# for i in range(9):
#     cpf += str(random.randint(0,9))

# print(cpf)
cpf_format =[]
for i in cpf:
    if i != '.' and i != '-':
        cpf_format.append(int(i))
        if len(cpf_format) == 9:
            break
    else:
        continue

soma_digito1 = 0
contador_regressivo_1 = 10

for numero in cpf_format:
    soma_digito1 += contador_regressivo_1 * int(numero) 
    contador_regressivo_1 -=1


digito_1 = (soma_digito1 *10) % 11 
digito_1 = digito_1 if digito_1 <= 9 else 0

contador_regressivo_2 = 11
#cpf = cpf + str(digito_1)
cpf_format.append(digito_1)
print(cpf)
soma_digito2 = 0
for numero in cpf_format:
    soma_digito2 += contador_regressivo_2 * int(numero)
    contador_regressivo_2 -= 1
digito_2 = (soma_digito2 * 10) % 11
digito_2 = digito_2 if digito_2 <=9 else 0
cpf_format.append(digito_2)
print(cpf_format)
# cpf_gerado = f"{cpf}{digito_2}"
# print(cpf_gerado)
cpf_formatado = ""
for i in cpf_format:
    cpf_formatado += str(i)
cpf_enviado = re.sub(
    r'[^0-9]','', cpf
)


print("CPF VÁLIDO"if cpf_formatado == cpf_enviado else "CPF INVÁLIDO")