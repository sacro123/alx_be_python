from datetime import datetime, timedelta

def display_current_datetime():
   
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
   
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=number_of_days)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")
    except ValueError:
        print("Error: Please enter a valid integer number of days.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
