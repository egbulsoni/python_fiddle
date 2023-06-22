import re

name = input("What's your name? ").strip()
# walrus operator ":=" allows assignment and asking the if
if matches := re.search(r"^(.+), *(.+)$", name):
    last, first = matches.groups()
    name = f"{first} {last}"
    # or use the one liner bellow
    # name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")
