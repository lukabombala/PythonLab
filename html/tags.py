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
    def both(_str, tag):
        return f"<{tag}>{_str}</{tag}>"

    def h1(self, _str):
        self.file.write(self.both(_str, "h1"))

    def p(self, _str):
        self.file.write(self.both(_str, "p"))
