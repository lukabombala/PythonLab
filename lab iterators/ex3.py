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


# testing
for elem in repeat(10, 3):
    print(elem, end=" ")

# for elem in repeat(5):
#    print(elem, end=" ")

# for elem in repeat(5, None):
#    print(elem, end=" ")
