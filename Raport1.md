

## Lista zadań 1: Generatory

### Zadanie 1
Poniższa funkcja jest implementacją wersji rozszerzonej zadania.
```python=
def even(n=0):
    while True:
        if n % 2 == 1:
            n += 1
        yield n
        n += 2
```
*Co powinno się stać, gdy użytkownik generatora jako wartość startową poda liczbę nieparzystą?*
\- Generator zacznie od kolejnej liczby parzystej

### Zadanie 2

```python=
def repeat(obj, times=None):
    count = 0
    while True:
        if count == times:
            break
        yield obj
        count += 1
```
### Zadanie 3
```python=
def accumulate(seq):
    _sum = seq[0]
    yield _sum
    for i in seq[1:]:
        _sum += i
        yield _sum
```
### Zadanie 4
Część 1:
```python=
def xrange(a=0, b=None):
    if b is None:
        b = a
        a = 0
    while a < b:
        yield a
        a += 1
```
Część 2:
```python=
for i in xrange(5, 15):
    print(i, end=" ")
```
## Lista zadań 2: Iteratory
### Zadanie 1
Część 1:
```python=
class count:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        x = self.n
        self.n += 1
        return x
```
Część 2:
```python=
def func():
    n = int(input("Podaj liczbę:"))

    cnt = count(n)
    for _ in range(10):
        print(next(cnt))
```
### Zadanie 2
Część 1:
```python=
class tetranacci:
    def __init__(self, steps):
        self.steps = steps
        self.elems = [0, 0, 0, 1]
        self.count = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == self.steps:
            raise StopIteration
        if self.count in {1, 2, 3}:
            self.count += 1
            return 0
        elif self.count == 4:
            self.count += 1
            return 1
        else:
            value = sum(self.elems)
            self.elems.append(value)
            self.elems.pop(0)
            self.count += 1
            return value
```
Część 2:
```python=
def func():
    n = int(input("Podaj wyraz ciągu tetranacciego:"))
    tet = tetranacci(20)
    for _ in range(n):
        print(next(tet))
```
### Zadanie 3
```python=
class repeat:
    def __init__(self, elem, times=None):
        self.elem = elem
        self.times = times
        self.count = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.times is not None:
            if self.count > self.times:
                raise StopIteration
        self.count += 1
        return self.elem
```
### Zadanie 4
```python=
class odd_first:
    def __init__(self, _list):
        self._list = _list
        self.ind = -1
        self._len = len(self._list)

    def __iter__(self):
        return self

    def __next__(self):
        self.ind += 2
        if (self.ind == self._len ) and (self._len % 2 == 0):
            raise StopIteration
        elif (self.ind == self._len + 1) and (self._len % 2 == 1):
            raise StopIteration
        elif self.ind >= self._len:
            self.ind = 0
        return self._list[self.ind]
```
### Zadanie 5
```python=
class chain:
    def __init__(self, *args):
        self._args = args
        self.ind = [0, 0]
        self.length = len(self._args)

    def __iter__(self):
        return self

    def __next__(self):
        if self.ind[0] == self.length:  # warunek stopu
            raise StopIteration
        _len = len(self._args[self.ind[0]])
        elem = self.ind.copy()
        if self.ind[1] == _len - 1:  # gdy dojdzemy do konca danej sekwencji, przechodzimy do następnego argumentu
            self.ind[0] += 1
            self.ind[1] = 0
        elif _len == 0:  # zabezpieczenie przeciwko wielokrotnym pustym sekwencjom
            self.ind[1] = 0
            while _len == 0:
                self.ind[0] += 1
                if self.ind[0] == self.length:
                    raise StopIteration
                _len = len(self._args[self.ind[0]])
                elem = self.ind.copy()
            self.ind[1] += 1
        else:
            self.ind[1] += 1  # przejscie od nastepnego elementu sekwencji
        return self._args[elem[0]][elem[1]]
```
