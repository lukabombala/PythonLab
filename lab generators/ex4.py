def xrange(*args):
    if len(args) == 1:
        a = 0
        b = args[0]
    else:
        a = args[0]
        b = args[1]

    while a < b:
        yield a
        a += 1


# testing
for i in xrange(5, 10):
    print(i, end=" ")
