def main():
    score = int(input("Enter Score: "))
    print(determine_score(score))


def determine_score(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def generate_score():
    import random
    score = random.randint(1, 100)
    print(f"{score} is {determine_score(score)}")


main()
# generate_score()
