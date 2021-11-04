# Raport 2 - Zaawansowany Python


## Lista zadań 3: Multithreading

### Zadanie 1
```python=
import threading


def thread_function(i, seq):
    thread_function._lock = threading.Lock()
    with thread_function._lock:
        for j in range(9):
            seq.append(10*i+j)


if __name__ == "__main__":
    output = []
    threads = []
    indices = [1, 3, 0, 2]
    for index in indices:
        x = threading.Thread(target=thread_function, args=(index, output))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        thread.join()
    print(output)

```

### Zadanie 2
```python=
import threading
import urllib.request
import urllib.error
import time


def thread_function(urls, lst):
    for url in urls:
        request = urllib.request.urlopen(url, timeout=30)
        lst.append((request, url))


def downloadpages(num):
    urls = [input(f"Podaj URL {i + 1}: ") for i in range(num)]
    print("Rozpoczynanie pobierania")

    output = []
    x = threading.Thread(target=thread_function, args=(urls, output))
    x.start()

    while x.is_alive():
        print("Oczekiwanie na zakończenie pobierania...")
        time.sleep(1)
    print("Wszystko pobrano.")
    for elem in output:
        print(f"Liczba znaków dla {elem[1]}: {len(elem[0].read())}")

if __name__ == "__main__":
    downloadpages(5)
```


### Zadanie 3
```python=
import threading
import hashlib
import uuid

identifiers = [uuid.uuid4().hex for _ in range(200)]


def thread_function(_hex, _dict):
    result = hashlib.md5(_hex.encode())
    _dict[_hex] = result.hexdigest()


if __name__ == "__main__":
    threads = []
    output = {}
    for hex_uuid in identifiers:
        x = threading.Thread(target=thread_function, args=(hex_uuid, output))
        threads.append(x)
        x.start()

    for thread in threads:
        thread.join()

    for key, value in output.items():
        print(f"{key} - {value}")
```