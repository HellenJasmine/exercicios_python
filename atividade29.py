

def fatorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1)

if __name__=="__main__":
    s = fatorial(5)
    print(s)