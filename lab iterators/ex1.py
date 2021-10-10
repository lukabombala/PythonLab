class Count:
    def __init__(self, n):
        self.n = n

    def __next__(self):
        self.n =+ 1
        return self.n - 1

def func():
    n = int(input("Podaj liczbę:"))

    for i in Count(n):
        print(i)
