import re

tested_str = None
while tested_str != "koniec":
    tested_str = input("Podaj napis: ")

    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    search = re.search(pattern, tested_str)

    if search:
        print("Email jest poprawny.")
    else:
        print("Email jest niepoprawny")
