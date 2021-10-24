import multiprocessing as mp
import time


def f(queue):
    while True:
        obj = queue.get()
        print(f"Proces potomny: {obj}")
        if obj == "exit":
            break


if __name__ == '__main__':
    q = mp.Queue()
    proc = mp.Process(target=f, args=(q,))
    proc.start()
    while True:
        time.sleep(1)
        if not proc.is_alive():
            proc.join()
            break
        _str = input("Podaj napis: ")
        q.put(_str)
