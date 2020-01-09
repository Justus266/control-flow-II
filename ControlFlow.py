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


"""
Programmer: Justus Boesch
Date: 1.7.20
Program: Average test scores

This program asks users how many tests they wish to average
"""

total = 0
how_many_tests = int(input("\nHow many tests would you like to average?: "))
print("")

for i in range(how_many_tests):
    enter_a_score = float(input("Enter a score: "))
    total = total + enter_a_score
   
average = total / how_many_tests
print("\nYour Average Test Scores Are: " + str(round(average, 2)))
