def xrange(a=0, b=None):
    if b is None:
        b = a
        a = 0
    while a < b:
        yield a
        a += 1


# testing
for i in xrange(5):
    print(i, end=" ")
