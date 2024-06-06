l1 = [1,2,3,4,5,6,7]
l2 = [1,2,3,4]
lista_soma = [x + y for x,y in zip(l1,l2)]

def soma_lista(l1,l2):
    lista_soma = []
    intervalo_maximo = min(len(l1), len(l2))
    for i in range(intervalo_maximo):
        lista_soma.append(l1[i] + l2[i])

    return lista_soma


print(soma_lista(l1,l2))
print(lista_soma)

