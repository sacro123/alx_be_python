task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        print(f"High priority task: {task}")
    case "medium":
        print(f"Medium priority task: {task}")
    case "low":
        print(f"Low priority task: {task}")
    case _:
        print("Invalid priority level entered.")

if time_bound == "yes":
    print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
else:
    print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
