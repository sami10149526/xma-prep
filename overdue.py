all_hours = [5, 72, 30.5, 49, 48, 120]
TARGET_HOURS = 24
total_overdue = 0

def is_overdue(hours_open, target):
    return hours_open > target

for hours in all_hours:
    if is_overdue(hours, TARGET_HOURS):
        print(f"Overdue: {hours} hours")
        total_overdue +=1

print(f"Total overdue tickets = {total_overdue}")

