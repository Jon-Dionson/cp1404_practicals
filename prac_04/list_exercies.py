# 1.
amount_of_numbers = 5
list_of_numbers = []

for i in range(5):
    number = int(input("Enter Number: "))
    list_of_numbers.append(number)

print(list_of_numbers)
print(f"The first number is {list_of_numbers[0]}")
print(f"The last number is {list_of_numbers[-1]}")
print(f"The smallest number is {min(list_of_numbers)}")
print(f"The largest number is {max(list_of_numbers)}")
print(f"The average of the numbers is {sum(list_of_numbers)/ amount_of_numbers}")


# 2.
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter username")
if username not in usernames:
    print("Access Granted")
else:
    print("Access Denied")

