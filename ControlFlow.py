# 2.3.20
#Greeting Function

#Declare Global Variable here.....

name = input("\nHello! What's your name?: ")
x = 15

#Create Functions Here.....

def greeting():
    print("\nHi There, " + name + "!")
    print("Very nice to meet you " + name)

def printSomething():
    x = 3
    print(x)


#Call Functions Here.....

greeting()
printSomething()
print(x)