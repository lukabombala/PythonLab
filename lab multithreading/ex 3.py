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
