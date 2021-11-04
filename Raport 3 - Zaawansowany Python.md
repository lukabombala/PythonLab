# Raport 3 - Zaawansowany Python
Imię i nazwisko: **Łukasz Bombała**
Nr indeksu: **76152**
Termin oddania pracy: **7.11.2021**

## Lista zadań 4: Multiprocessing

### Zadanie 1

```python=
import multiprocessing

print(multiprocessing.cpu_count())

```

### Zadanie 2

```python=
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
    
```

### Zadanie 3

```python=
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

```

### Zadanie 4

```python=
import multiprocessing as mp


def f(x):
    return x**2


if __name__ == '__main__':
    num = [int(i) for i in input("Podaj 10 liczb oddzielonych spacją: ").split(" ")]
    with mp.Pool(5) as p:
        output = p.map(f, num)

    print(output)

```

### Zadanie 5

```python=
import hashlib
import uuid
import multiprocessing as mp


def function(_hex, ):
    result = hashlib.md5(_hex.encode())
    return _hex, result.hexdigest()


if __name__ == "__main__":
    identifiers = [uuid.uuid4().hex for _ in range(200)]

    with mp.Pool(10) as p:
        output = p.map(function, identifiers)
    for elem in output:
        print(f"{elem[0]} - {elem[1]}")
        
```