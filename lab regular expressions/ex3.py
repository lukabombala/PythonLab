import re

tested_str = None
while tested_str != "koniec":
    tested_str = input("Podaj napis: ")

    pattern = r"^#(?:[0-9a-fA-F]{3}){1,2}$"
    search = re.search(pattern, tested_str)

    if search:
        print("Napis poprawny.")
    else:
        print("Napis niepoprawny")
