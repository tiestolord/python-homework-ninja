# Calculator

x = int(input("Enter the number: "))
y = int(input("Enter the number: "))

calculator = input("Choose the operation: ")

if calculator == "+":
    print(x+y)

elif calculator == "-":
    print(x-y)

elif calculator == "*":
    print(x*y)

elif calculator == "/":
    print(x/y)