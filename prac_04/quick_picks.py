
import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45

amount_of_quick_picks = int(input("How many quick picks: "))
while amount_of_quick_picks < 0:
    print("please enter an amount larger than 0")
    amount_of_quick_picks = int(input("How many quick picks: "))

for i in range(amount_of_quick_picks):
    quick_picks = []
    for j in range(NUMBERS_PER_LINE):
        number = random.randint(MINIMUM, MAXIMUM)
        while number in quick_picks:
            number = random.randint(MINIMUM, MAXIMUM)
        # print(number, end=" ")
        quick_picks.append(number)
    quick_picks.sort()
    print(quick_picks)
