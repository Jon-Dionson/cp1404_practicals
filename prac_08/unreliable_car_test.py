"""Test file for UnreliableCar class"""

from prac_08.unreliable_car import UnreliableCar

reliability = int(input("enter reliability: "))
my_car = UnreliableCar("test car", 100, reliability)
print(my_car.drive(100))

for i in range(1, 11):
    print(f"{i}km will be driven")
    print()
    print(f"{my_car.name} drove {my_car.drive(i)}km")
print(my_car)
