def genrange(start, end):
    for i in range(start, end + 1):
        yield i

#test code
print(list(genrange(1, 10)))