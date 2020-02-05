
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
