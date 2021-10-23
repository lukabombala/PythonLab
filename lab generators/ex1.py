import time


def even(n=0):
    while True:
        if n % 2 == 1:
            n += 1
        yield n
        n += 2


# testing
for i in even(5):
    print(i)
    time.sleep(0.5)
