"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """run the program"""
    data = get_data()
    print(data)
    display_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        data.append(parts)
    input_file.close()
    return data


def display_subject_details(data):
    """formats subject data"""
    for subject_data in data:
        subject = subject_data[:1]
        teacher = subject_data[1:2]
        students = subject_data[-1:]
        print(f"{subject}is taught by {teacher} and has {students} students")
    # for subject_data in data:
    #     print("{} is taught by {:12} and has {:3} students".format(*subject_data))


main()
