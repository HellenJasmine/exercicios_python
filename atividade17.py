import sys

iterable = ['eu', 'tenho', '__inter__']
iterator = iter(iterable)
lista = [n for n in range(100)]
generator = (i for i in range (100))
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))