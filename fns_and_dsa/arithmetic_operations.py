# main.py
from arithmetic_operations import perform_operation
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
