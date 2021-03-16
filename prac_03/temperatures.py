"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """run the program"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            convert_to_fahrenheit(celsius)
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            convert_to_celsius(fahrenheit)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_to_fahrenheit(celsius):
    """convert celsius to fahrenheit"""
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))


def convert_to_celsius(fahrenheit):
    """convert fahrenheit to celsius"""
    celsius = 5 / 9 * (fahrenheit - 32)
    print("Result: {:.2f} C".format(celsius))


main()
