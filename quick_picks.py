import random
AMOUNT_OF_NUMBERS = 6
MINIMUM = 1
MAXIMUM = 45

amount_of_quick_picks = int(input("How many quick picks: "))
while amount_of_quick_picks < 0:
    print("please enter an amount larger than 0")
    amount_of_quick_picks = int(input("How many quick picks: "))

for i in range(amount_of_quick_picks):
    quick_pick = []
    for j in range(AMOUNT_OF_NUMBERS):
        number = random.randint(MINIMUM, MAXIMUM)
        while number in quick_pick:
            number = random.randint(MINIMUM, MAXIMUM)
        print(number, end=" ")
        quick_pick.append(number)

print()

