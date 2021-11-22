import re

tested_str = input("Podaj napis: ")

pattern = r"^\d+$"
search = re.search(pattern, tested_str)

if not search:
    print("To nie jest liczba.")
else:
    print("To jest liczba")
