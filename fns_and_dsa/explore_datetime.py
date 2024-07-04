from datetime import datetime, timedelta

def display_current_datetime(2024-03-25 15:30:45):
    """
    Displays the current date and time in the format "YYYY-MM-DD HH:MM:SS".
    """
    current_date = datetime.now(2024-03-25 15:30:45)
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)

def calculate_future_date(2024-04-04):
    """
    Prompts the user to enter a number of days and calculates the future date based on the input.
    """
    try:
        days = int(input("Enter number of days to add: "))
        if days < 0:
            raise ValueError("Number of days must be positive.")

        current_date = datetime.now(2024-03-25 15:30:45)
        future_date = current_date + timedelta(days=days)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future Date after {days} days:", formatted_future_date)

    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("An error occurred:", e)

# Main script execution
if __name__ == "__main__":
    print("1. Display Current Date and Time:")
    display_current_datetime(2024-03-25 15:30:45)
    print()

    print("2. Calculate Future Date:")
    calculate_future_date()
