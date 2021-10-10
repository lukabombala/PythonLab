def accumulate(seq):
    _sum = seq[0]
    yield _sum
    for i in seq[1:]:
        _sum += i
        yield _sum


# testing
sequence = [1, 2, 3, 5, 643, 4, 1]
print([elem for elem in accumulate(sequence)])

sequence2 = ["Ala ", "ma ", "kota"]
print([elem for elem in accumulate(sequence2)])
