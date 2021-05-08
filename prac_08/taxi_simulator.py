"""Taxi simulator program"""
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            taxi_choice = get_valid_number("Choose taxi: ", taxis)
            print(taxi_choice)
        elif choice == "d":
            print("drive taxi")
        else:
            print("Invalid option")
            print(f"Bill to date: {bill}")
        print(MENU)
        choice = input(">>> ").lower()


def get_valid_number(prompt, taxis):
    """get valid taxi number"""
    finished = False
    while not finished:
        try:
            number = int(input(prompt))
            while number < 0:
                print("Number must be > 0")
                number = int(input(prompt))
            while number > len(taxis):
                print("Invalid taxi choice")
                number = int(input(prompt))
            finished = True
        except ValueError:
            print("Invalid input; enter a valid number")
        for taxi in taxis:
            return taxi


main()
