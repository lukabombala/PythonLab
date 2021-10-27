class document:
    def __init__(self,
                 title,
                 doctype="<!DOCTYPE html>"):

        self.title = title
        self.doctype = doctype

    @property
    def file(self):
        return self._file

    def __enter__(self):
        self._file = open(f"{self.title}.html", "w")
        self.file.write(f"{self.doctype}\n<html lang=''>\n")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.write("</html>\n")
        self._file.close()

    def head(self):
        lines = [
            "<head>\n",
            f"<title>{self.title}</title>\n",
            "</head>\n",
        ]
        self._file.writelines(lines)
