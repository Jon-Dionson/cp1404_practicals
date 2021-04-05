COLOURS = {"aquamarine2": "#76eec6", "beige": "#f5f5dc", "gray": "#bebebe", "green1": "#00ff00", "green2": "#00ee00",
           "honeydew1": "#f0fff0", "LightCoral": "#f08080", "ivory1": "#fffff0", "LightGray": "#d3d3d3",
           "LightPink": "#ffb6c1"}
choice = input("Enter colour name: ")
while choice != "":
    if choice in COLOURS:
        print(f"the hex code for {choice} is {COLOURS[choice]}")
    else:
        print("colour not in list")
    choice = input("Enter colour name: ").lower()
