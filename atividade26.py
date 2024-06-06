from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas =[
    'João', 'Joana', 'Luiz','Hellen'
]

camisetas = [
    ['preta', 'branca'],
    ['p','m'],
    ['masculino', 'feminino','unissex'],
    ['algodão', 'poliéster']
]

print_iter(combinations(pessoas, 2))
print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))