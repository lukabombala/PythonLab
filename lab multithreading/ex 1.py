import threading


def thread_function(i, seq):
    thread_function._lock = threading.Lock()
    with thread_function._lock:
        for j in range(10):
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
