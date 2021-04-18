from prac_06.guitar import Guitar
guitars = []
print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)
    print(f"{new_guitar} added.")
    name = input("Name: ")

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))


print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage_string = ""
    if guitar.is_vintage():
        vintage_string = "(vintage)"
    print(f"Guitar {i}: {guitar}, {vintage_string}")

