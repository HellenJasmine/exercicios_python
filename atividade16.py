# string = 'Hellen'
# if hasattr(string,'upper' ):
#     print("Existe upper")
#     print(string.upper())


string = 'Hellen'
metodo = 'upper'

if hasattr(string, metodo):
    print("existe upper")
    print(getattr(string, metodo)())
    print(string)