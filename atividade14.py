lista = [
    i for i in range(10) if i < 6
]
print(lista)

# produtos = {
#     {'nome':'arroz', 'preco': 10},
#     {'nome': 'feijao', 'preco':10},
#     {'nome': 'macarrao', 'preco':10},
# }

# new_products = [
#     product 
#     for product in produtos
# ]
# print(new_products)

produto = {
    'nome': 'Caneta',
    'preco': 2.5,
    'categoria':'Escritório',
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor 
    in produto.items()
    if chave == 'categoria'
}
print(dc)