num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("Choose operatin (+, -, *, /): ")

match operation:
    case '+':
        add = num1 + num2
        print("The result is", add)
    case '-':
        sub = num1 - num2
        print("The result is", sub)
    case '*':
        mul = num1 * num2
        print("The result is", mul)
    case '/':
        if(num1 == 0 or num2 == 0):
            print("Cannot divide by zero")
        div = float(num1) / float(num2)
        print("The result is", div)
    case _:
        print("Invalid entry")