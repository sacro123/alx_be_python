def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations (+, -, *, /) on num1 and num2 based on the operation parameter.

    Parameters:
    - num1 (float): The first operand.
    - num2 (float): The second operand.
    - operation (str): The arithmetic operation to perform. Possible values: 'add', 'subtract', 'multiply', 'divide'.

    Returns:
    - float or str: The result of the arithmetic operation. Returns an error message for division by zero.
    """
    result = None
    
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
    if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
        else:
        result = "Error: Invalid operation"
    
    return result

from arithmetic_operations import perform_operation

def main():
    # Example usage of perform_operation function
    num1 = 10.0
    num2 = 3.0
    
    # Addition
    print(f"{num1} + {num2} = {perform_operation(num1, num2, 'add')}")
    
    # Subtraction
    print(f"{num1} - {num2} = {perform_operation(num1, num2, 'subtract')}")
    
    # Multiplication
    print(f"{num1} * {num2} = {perform_operation(num1, num2, 'multiply')}")
    
    # Division
    print(f"{num1} / {num2} = {perform_operation(num1, num2, 'divide')}")
    
    # Division by zero example
    print(f"{num1} / 0 = {perform_operation(num1, 0, 'divide')}")
    
    # Invalid operation example
    print(f"{num1} # {num2} = {perform_operation(num1, num2, 'invalid')}")

if __name__ == "__main__":
    main()
    python main.py
