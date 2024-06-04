import sys
print(sys.platform)

try:
    a = 18
    b = 0
    print('linha1'[132])
    c = a/b
except ZeroDivisionError:
    print("dividiu por 0")
except NameError:
    print("nome b nao esta definido")
except (TypeError, IndexError) as error:
    print("typeError + indexError")
    print("mensagem:", error)
    print("nome:" , error.__class__.__name__)
except Exception:
    print("Erro desconhecido")

print('continuar')