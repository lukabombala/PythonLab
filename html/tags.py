class body:
    def __init__(self, file):
        self.file = file

    def __enter__(self):
        self.file.write("<body>\n")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.write("\n</body>\n")
        if any([exc_type, exc_val, exc_tb]):
            print(exc_type, exc_val, exc_tb, sep="\n")

    @staticmethod
    def both(_str, tag, end="\n"):
        return f"<{tag}>{_str}</{tag}>{end}"

    def h1(self, _str, **kwargs):
        self.file.write(self.both(_str, "h1", [kwargs['end'] if kwargs else "\n"][0]))

    def p(self, _str, **kwargs):
        self.file.write(self.both(_str, "p", [kwargs['end'] if kwargs else "\n"][0]))
