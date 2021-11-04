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


downloadpages(5)
