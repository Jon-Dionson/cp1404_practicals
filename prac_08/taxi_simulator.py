"""Taxi simulator program"""
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    current_taxi = " "
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available")
            display_taxis(taxis)
            current_taxi = get_valid_taxi("Choose taxi: ", taxis)
            print(taxis[current_taxi])

        elif choice == "d":
            if current_taxi == " ":
                print("You need to choose a taxi before you can drive")
            else:
                # get kilometers
                # get fare
                # add fare to total_bill
                pass

        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def get_valid_taxi(prompt, taxis):
    """get valid taxi"""
    finished = False
    number = 0
    while not finished:
        try:
            number = int(input(prompt))
            while number < 0:
                print("Number must be > 0")
                number = int(input(prompt))
            while number >= len(taxis):
                print("Invalid taxi choice")
                number = int(input(prompt))
            finished = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return number


main()
