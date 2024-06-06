# def criar_funcao(func):
#     def interna(*args,**kwargs):
#         for arg in args:
#             e_string(arg)

#         resultado = func(*args, **kwargs)
#         return resultado
#     return interna

# @criar_funcao
# def inverte_string(string):
#     return string[::-1]

# def e_string(param):
#     if not isinstance(param, str):
#         raise TypeError("param deve ser yma string")



# invertida = inverte_string("Hellen")
# print(invertida)

def decoradora(func):
    print("Decoradora 1")

    def aninhada(*args, **kwargs):
        print(args, kwargs)
        print("aninhada")
        res = func(*args, **kwargs)
        return res
    return aninhada


@decoradora
def soma(x,y):
    return x + y


dez_mais_cinco = soma(10,5)
print(dez_mais_cinco)