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


# Date: 2.3.20
# Programmer: Justus

#Declare Global Variable here.....

name = input("\nHello! What's your name?: ")
x = 15

#Create Functions Here.....

# Greeting Function
def greeting():
    print("Hi There, " + name + "!")
    print("Very nice to meet you " + name)

# Fucntions & Local Variables "x"
def printSomething():
    x = 3
    print(x)

# Functions & Parameters
def printNumber(age): #function name = printNumber with a PARAMETER of "age"
    print(age)

# Defualt Parameters Values
def printTwoNumbers(x, y = 71):
    print("First Parameter(Number): " + str(x))
    print("Second Parameter(Number): " + str(y))

# Print Sum
def printSum(x,y):
    print(x + y)

# Print Multiple Times
def printMultipleTimes(string, times):
    for i in range(times):
        print(string)

#Call Functions Here.....

print("\n****Greetings Function****\n")
greeting()

print("\n****Print Something Function****\n")
printSomething()

# print(x)Showing Global Variable

print("\n****Print Number Function****\n")
printNumber(28)
printNumber(38)

print("\n****Print Two Numbers Function****\n")
printTwoNumbers(23,78)

print("\n****Default Parameter Values Function****\n")
printTwoNumbers(45)

print("\n****Print Sum Function****\n")
printSum(36,29)

print("\n****Print Multiple Times Function****\n")
printMultipleTimes("I love Computer Science", 13)

print("\nThank you for hanging out with me through all my Functions being called!")

