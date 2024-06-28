# multiplication_table.py

def print_multiplication_table():
    # Prompt the user for a number
    number = int(input("Enter a number to see its multiplication table: "))

    # Generate and print the multiplication table
    for i in range(1, 10):
        print(f"{number} * {i} = {number * i}")

# Call the function to execute the script
print_multiplication_table()
python3 multiplication_table.py
