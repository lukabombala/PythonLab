class chain:
    def __init__(self, *args):
        self._args = args

    def __iter__(self):
        return self

    def __next__(self):
        pass
