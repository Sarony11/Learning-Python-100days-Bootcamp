# We can try to print and construct a table, but in the way we now as far, is a bit complex
print("| Pokemon Name | Type |")
print("_______________________")
print("| Charmander   | Fire |")
print("_______________________")

# However, we can import a packet made from another programmer
# pypi.org

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon", ["Charmander", "Squirtle", "Pikachu", "Io"])
table.add_column("Type", ["Fire", "Water", "Electrical", "Seven"])
table.align = "l"
print(table)


