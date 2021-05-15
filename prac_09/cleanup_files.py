"""
CP1404/CP5632 Practical
Cleanup files program
"""
import shutil
import os


def main():
    """Tidy up song titles to be consistent"""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = ""
    # new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    for i, character in enumerate(filename):
        if character == " ":
            new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
        #     and change next char to is.upper()
        # if char is.lower() followed by char is.upper(),
        #   add '_' between the two
    return new_name


main()
