"""
Programmer: Justus Boesch
Date: 12.16.19
Program: Guess My Number
"""



myNumber = 7

print("\nGuess a number between 1 & 10\n")

# Ask users to guess
guess = int(input("Enter a Guess: "))

# Keep asking users to guess my number until it is equal to myNumber
while guess != myNumber:
    print("\nNope, guess again: ")
    guess = int(input("Enter a Guess: "))

print("\nCongradulations! you guessed my number!")


# Programmer: Justus Boesch
# Date: 1.20.20
# Program: Double For Loop

for i in range(3):
    print("Outer For Loop" + str(i))
    for k in range(4):
        print("\tInner For Loop" + str(k))

print("\n*******************\n")



"""
Programmer: Justus Boesch
<<<<<<< HEAD
Date: 12.19.19
Program: 1 through 10
"""

x = 1

# While loop will see if a condition has been met
# If not it will run again until the condition
# has been met

while x <= 10:
    print(x)
    x+=1


"""
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

"""
Date: 1.23.20
Program: While Loop nested inside a For Loop
"""

for i in range(4):
    print("For Loop: " + str(i))
    x = i
    while x >= 0:
        print("\tWhile Loop: " + str(x))
        # x = x - 1
        x = x - 1

