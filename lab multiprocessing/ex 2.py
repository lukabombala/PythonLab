from multiprocessing import Process
import os


def f():
    print(os.getpid())


if __name__ == '__main__':
    print(os.getpid())

    p1 = Process(target=f)
    p2 = Process(target=f)

    p1.start()
    p2.start()
    p1.join()
    p2.join()
