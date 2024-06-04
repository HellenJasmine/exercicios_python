def generator(n=0, maximun = 10):
    while True:
        yield n
        n +=1

        if n > maximun:
            return





g = generator()
for n in g:
    print(n)
