class odd_first:
    def __init__(self, _list):
        self._list = _list
        self.ind = -2
        self._len = len(self._list)

    def __iter__(self):
        return self

    def __next__(self):
        self.ind += 2
        if self.ind == self._len-1:
            raise StopIteration
        elif self.ind > self._len-1:
            self.ind = 1
        return self._list[self.ind]


# testing
for elem in odd_first([1, 2, 3, 4, 5, 6]):
    print(elem, end=" ")
print("\n")
for elem in odd_first(["A", "B", "C", "D", "E", "F"]):
    print(elem, end=" ")
