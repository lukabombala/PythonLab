import hashlib
import uuid
import multiprocessing as mp

identifiers = [uuid.uuid4().hex for _ in range(200)]


def function(_hex, _dict):
    result = hashlib.md5(_hex.encode())
    _dict[_hex] = result.hexdigest()


if __name__ == "__main__":
    processes = []
    output = {}
    for hex_uuid in identifiers:
        x = mp.Process(target=function, args=(hex_uuid, output))
        processes.append(x)
        x.start()

    for process in processes:
        process.join()

    for key, value in output.items():
        print(f"{key} - {value}")
