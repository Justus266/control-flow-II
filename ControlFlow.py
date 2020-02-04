
# Date: 2.3.20
# Programmer: Justus

#Declare Global Variable here.....

# name = input("\nHello! What's your name?: ")
x = 15

#Create Functions Here.....

# Greeting Function
def greeting():
    print("\nHi There, " + name + "!")
    print("Very nice to meet you " + name)

# Fucntions & Local Variables "x"
def printSomething():
    x = 3
    print(x)

# Functions & Parameters
def printNumber(age): #function name = printNumber with a PARAMETER of "age"
    print(age)


#Call Functions Here.....

# greeting()
# printSomething()
# print(x)
printNumber(28)
printNumber(38)