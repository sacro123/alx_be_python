def calculator():
    # Asking the user to input two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Asking for the type of operation
    operation = input("Choose the operation (+, -, *, /): ").strip()

    # Performing the calculation using match case
    match operation:
        case '+':
            result = num1 + num2
            print(f"The result is {result}.")
        case '-':
            result = num1 - num2
            print(f"The result is {result}.")
        case '*':
            result = num1 * num2
            print(f"The result is {result}.")
        case '/':
            if num2 != 0:
                result = num1 / num2
                print(f"The result is {result}.")
            else:
                print("Error: Division by zero is not allowed.")
        case _:
            print("Invalid operation. Please choose from +, -, *, /.")

# Calling the calculator function to execute the script
calculator()
