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

    def both(self, _str, tag, end):
        self.file.write(f"<{tag}>{_str}</{tag}>{end}")

    def br(self):
        self.file.write("<br>")

    def h1(self, _str, end="\n"):
        self.both(_str, tag="h1", end=end)

    def h2(self, _str, end="\n"):
        self.both(_str, tag="h2", end=end)

    def h3(self, _str, end="\n"):
        self.both(_str, tag="h3", end=end)

    def p(self, _str, end="\n"):
        self.both(_str, tag="p", end=end)

    def data_table(self,
                   data,
                   top_header=True,
                   header=None,
                   end="\n",
                   style=None):
        """Creates simple html table from 2d data matrix"""

        if style is None:
            style = ""
        else:
            temp = [f"{key}: {value}" for key, value in style.items()]
            style = ";".join(temp)

        self.file.write(f'<table style=\"{style}\">\n')
        if top_header is True:
            self.file.write('<tr>\n')
            for elem in data[0]:
                self.both(elem, "th", end="\n")
            self.file.write('</tr>\n')
            for row in data[1:]:
                self.file.write('<tr>\n')
                for elem in row:
                    self.both(elem, tag="td", end=end)
                self.file.write('<tr>\n')
        else:
            if header is not None:
                self.file.write('<tr>\n')
                for elem in header:
                    self.both(elem, "th", end="\n")
                self.file.write('</tr>\n')
            if not isinstance(data[0], list):
                self.file.write('<tr>\n')
                for elem in data:
                    self.both(elem, tag="td", end=end)
                self.file.write('</tr>\n')
            else:
                for row in data:
                    self.file.write('<tr>\n')
                    for elem in row:
                        self.both(elem, tag="td", end=end)
                    self.file.write('</tr>\n')
        self.file.write(f'</table>{end}')
