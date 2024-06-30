def get_task_details():
    task = input("Enter the task description: ")
    priority = input("Enter the task's priority (high, medium, low): ").lower()
    time_bound = input("Is the task time-bound? (yes or no): ").lower()
    return task, priority, time_bound

def process_task(task, priority, time_bound):
    reminder = ""

    match priority:
        case "high":
            reminder = f"High priority task: {task}"
        case "medium":
            reminder = f"Medium priority task: {task}"
        case "low":
            reminder = f"Low priority task: {task}"
        case _:
            reminder = f"Task: {task}"

    if time_bound == "yes":
        reminder += " that requires immediate attention today!"

    return reminder

def main():
    task, priority, time_bound = get_task_details()
    reminder = process_task(task, priority, time_bound)
    print(reminder)

if __name__ == "__main__":
    main()
