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


a = chain("abc", [], [1, 2, 3], "DEF", [], [], [], [], [], [], [], "", [1, 2, 3])

for e in a:
    print(e, end=" ")
