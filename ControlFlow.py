"""
Programmer: Justus Boesch
Date: 1.6.20
Program: Running Total

This Program asks users for five numbers
It then sums up the numbers
"""

sum = 0

for i in range(5):
    enter_a_number = int(input("Enter a number: "))
    sum = sum + enter_a_number

print("\nSum of your numbers is: " + str(sum))