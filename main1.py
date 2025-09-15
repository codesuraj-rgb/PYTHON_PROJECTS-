import math

operation = ["+,-,/,*"]

while True:
    num1 = float(input("Enter the number : "))
    num2 = float(input("Enter the number : "))

    print("Choose an operation to perform:")
    print("+ for Addition")
    print("- for Subtraction")
    print("* for Multiplication")
    print("/ for Division")

    operation = input("Enter operation (+, -, *, /): ")
    if operation in ["+", "-", "*", "/"]:
        print("You selected operation:", operation)
    else:
        print("Invalid operation! Please enter +, -, *, or /.")

    def add():
        if operation == "+":
            print(num1 + num2)
    def subtract():
        if operation == "-":
            print(num1 - num2)
    def multiply():
        if operation == "*":
            print(num1 * num2)
    def divide():
        if operation == "/":
            if(num2!=0):
                print(num1/num2)
            else:
                print("cannot divide by zero")
    
    if operation == "+":
        add()
    elif operation == "-":
        subtract()
    elif operation == "*":
        multiply()
    elif operation == "/":
        divide()

    again = input("Do you want to perform another calculation? (yes/no): ")
    if again.lower() != "yes":
        print("Goodbye!")
        break
    


     


