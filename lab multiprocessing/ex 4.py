import multiprocessing as mp


def f(x):
    return x**2


if __name__ == '__main__':
    num = [int(i) for i in input("Podaj 10 liczb oddzielonych spacją: ").split(" ")]
    with mp.Pool(5) as p:
        output = p.map(f, num)

    print(output)
