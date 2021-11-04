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
