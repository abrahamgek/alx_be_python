# Prompt for a single task
task = input("Enter your task: ")
# Prompt for the task's priority
priority = input("Priority (high/medium/low): ")
# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ")
# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"High priority task: {task}"
    case "medium":
        reminder = f"Medium priority task: {task}"
    case "low":
        reminder = f"Low priority task: {task}"
    case _:
        reminder = f"Task: {task} (priority not specified correctly)"
# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
# Provide a customized reminder
print(f"Reminder:\n{reminder}")