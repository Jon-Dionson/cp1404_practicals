MIN_LENGTH = 3
MAX_LENGTH = 10


def main():
    """run"""
    password = get_password()
    check_password(password)


def get_password():
    """get the user's password"""
    password = input("Enter a password: ")
    return password


def check_password(password):
    """check the user's password"""
    while len(password) > MAX_LENGTH or len(password) < MIN_LENGTH:
        print("Invalid Password")
        password = input("Enter a password: ")
    print(len(password) * "*")


main()
