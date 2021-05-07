"""Taxi simulator program"""
# from prac_08.silver_service_taxi import SilverTaxi
MENU = "q)uit, c)hoose taxi, d)rive"

print("Let's drive!")
print(MENU)
choice = input(">>> ").lower()
while choice != "q":
    if choice == "c":
        print("Taxis available")
    elif choice == "d":
        print("drive taxi")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").lower()
