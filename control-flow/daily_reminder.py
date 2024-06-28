# task_reminder.py

def get_task_details():
    # Prompt the user for a task description
    task = input("Enter the task description: ")

    # Prompt for the task's priority
    priority = input("Enter the task's priority (high, medium, low): ").lower()

    # Prompt if the task is time-bound
    time_bound = input("Is the task time-bound? (yes or no): ").lower()

    return task, priority, time_bound

def process_task(task, priority, time_bound):
    reminder = ""

    # Use a match case to react differently based on the task's priority
    match priority:
        case "high":
            reminder = f"High priority task: {task}"
        case "medium":
            reminder = f"Medium priority task: {task}"
        case "low":
            reminder = f"Low priority task: {task}"
        case _:
            reminder = f"Task: {task}"

    # Use an if statement to modify the reminder if the task is time-bound
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"

    return reminder

def main():
    # Get task details from the user
    task, priority, time_bound = get_task_details()

    # Process the task and get the reminder
    reminder = process_task(task, priority, time_bound)

    # Print the customized reminder
    print(reminder)

# Execute the script
if __name__ == "__main__":
    main()
