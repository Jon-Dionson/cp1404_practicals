from prac_06.guitar import Guitar
CURRENT_YEAR = 2021
name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

first_guitar = Guitar(name, year, cost)
second_guitar = Guitar("Another Guitar", 2013, 1234)
third_guitar = Guitar("50 year old guitar", CURRENT_YEAR - 50, 575)
print(f"{first_guitar.name} get_age() - Expected 98. Got {first_guitar.get_age()}")
print(f"{second_guitar.name} get_age() - Expected 8. Got {second_guitar.get_age()}")
print(f"{first_guitar.name} is_vintage() - Expected True.  Got {first_guitar.is_vintage()}")
print(f"{second_guitar.name} is_vintage() - Expected False.  Got {second_guitar.is_vintage()}")
print(f"{third_guitar.name} is_vintage() - Expected True. Got {third_guitar.is_vintage()}")
