def repeat(n, times=None):
    count = 0
    while True:
        if count == times:
            break
        yield n
        count += 1


# testing
for elem in repeat(10, 5):
    print(elem, end=" ")

for elem in repeat(10):
    print(elem, end=" ")
