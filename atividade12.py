def exponenciar_ao_quadrado(numero):
    return numero * numero


def exponenciar_ao_cubo(numero):
    return numero*numero*numero


def duplicar_numero(numero):
    return numero * 2


def triplicar_numero(numero):
    return numero * 3


def quadruplicar_numero(numero):
    return numero * 4

def criar_multiplicador(multiplicador):
    def multiplicacao(numero):
        return numero * multiplicador
    return multiplicacao


print(exponenciar_ao_quadrado(5))
print(exponenciar_ao_cubo(5))
print(duplicar_numero(5))
print(triplicar_numero(5))
print(quadruplicar_numero(5))

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)
print(duplicar(10))
print(triplicar(10))
print(quadruplicar(10))