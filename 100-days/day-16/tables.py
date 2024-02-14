from prettytable import PrettyTable

table = PrettyTable()
print(table)
table.field_names = ["Pokemon", "Type"]
table.add_rows([["pikachu", "electric"], ["ratata", "normal"], ["charmander", "fire"], ["totodile", "water"], ["chicorita", "grass"]])
table.align = "l"

print(table)