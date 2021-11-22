import re

tested_str = None
while tested_str != "koniec":
    tested_str = input("Podaj napis: ")

    pattern = r"^[0-9]{2}-[0-9]{3}$"
    search = re.search(pattern, tested_str)

    if search:
        print("Kod jest poprawny.")
    else:
        print("kod jest niepoprawny")
