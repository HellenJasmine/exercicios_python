def concatenar(string_incial):
    valor_final = string_incial

    def interna(valor_a_concatenar = ''):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna

c = concatenar("H")
print(c("e"))
print(c("l"))
print(c("l"))
print(c("e"))
print(c("n"))

final = c()
print(final)