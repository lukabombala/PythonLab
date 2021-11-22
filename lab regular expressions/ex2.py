import re

tested_str = input("Podaj napis: ")

pattern = r"\d{1}"
search = re.findall(pattern, tested_str)

print(f"Znalezione liczby: {search}")
