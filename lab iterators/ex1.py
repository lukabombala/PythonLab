class count:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        x = self.n
        self.n += 1
        return x


def func():
    n = int(input("Podaj liczbę:"))

    cnt = count(n)
    for _ in range(10):
        print(next(cnt))


# testing
func()
