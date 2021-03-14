def main():
    import random
    out_file = open("results.txt", "w")
    number_of_scores = int(input("How many scores: "))
    for i in range(number_of_scores):
        score = random.randint(1, 100)
        print(f"{int(score)} is {determine_score(score)}")
        print(f"{score} is {determine_score(score)}", file=out_file)
    out_file.close()


def determine_score(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
