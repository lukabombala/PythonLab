class tetranacci:
    def __init__(self, steps):
        self.steps = steps
        self.elems = [0, 0, 0, 1]
        self.count = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == self.steps:
            raise StopIteration
        if self.count in {1, 2, 3}:
            self.count += 1
            return 0
        elif self.count == 4:
            self.count += 1
            return 1
        else:
            value = sum(self.elems)
            self.elems.append(value)
            self.elems.pop(0)
            self.count += 1
            return value


def func():
    n = int(input("Podaj wyraz ciągu tetranacciego:"))
    tet = tetranacci(20)
    for _ in range(n):
        print(next(tet))


# testing
func()
