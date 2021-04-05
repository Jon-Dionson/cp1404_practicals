def main():
    email_to_name = {}
    email = input("Email: ")

    while email != "":
        name = get_name_from_email(email)
        confirm_name = input(f"Is your name {name} (Y/n) ")
        if confirm_name.upper() != "Y" and confirm_name != "":
            name = input("Name")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    full_name = email.split("@")[0]
    parts = full_name.split(".")
    formatted_name = " ".join(parts).title()
    return formatted_name


main()
