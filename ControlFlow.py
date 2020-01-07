"""
Programmer: Justus Boesch
Date: 1.6.20
Program: Running Total, part II

This Program asks users for five numbers
It then sums up the numbers
"""

sum = 0
how_many_numbers = int(input("\nHow many numbers would you like to sum up?: "))
print("")

for i in range(how_many_numbers):
    enter_a_number = int(input("\nEnter a number: "))
    sum = sum + enter_a_number

print("\nSum of your numbers is: " + str(sum))