import threading
import urllib.request
import urllib.error
import time


def thread_function(url, lst):
    request = urllib.request.urlopen(url, timeout=30)
    lst.append(request)


def downloadpages(num):
    urls = [input(f"Podaj URL {i + 1}: ") for i in range(num)]
    print("Rozpoczynanie pobierania")
    threads = []
    outputs = []
    for url in urls:
        x = threading.Thread(target=thread_function, args=(url, outputs))
        threads.append(x)
        x.start()
    stop = all([thread.is_alive() for thread in threads])
    while not stop:
        print("Oczekiwanie na zakończenie pobierania...")

downloadpages(5)
