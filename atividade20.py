import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

products_update_value = [
    {'nome': produto['nome'], 'preco': produto['preco']*1.1}
    for produto in produtos

]
produtos_copiados = [
    {'nome': produto['nome'], 'preco': round(produto['preco']*1.1, 2)}
    for produto in copy.deepcopy(produtos)
    
]

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda produto: produto['nome']
)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda produto: produto['preco']
)


print(*produtos_copiados, sep="\n")
print()
print(*produtos_ordenados_por_nome, sep="\n")
print()
print(*produtos_ordenados_por_preco, sep="\n")