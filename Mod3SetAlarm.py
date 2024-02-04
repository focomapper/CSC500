# Get time from user and validate that it's a whole number
try:
    current_time_hours = (int(input("Enter time in hours: ")))
except ValueError:
    print("Your input was not a whole number (hours), run program again and enter valid number")
    exit()

# Make sure time entered is 23 or less
if not (23 > current_time_hours >= 0):
    print("Your input must be from 0 to 23, run program again and enter valid time")
    exit()

# Get time to wait for alarm from user and validate that it's a number
try:
    wait_time_hours = (int(input("Enter hours to wait for alarm: ")))
except ValueError:
    print("Your input was not a number (hours), run program again and enter valid number")
    exit()

# Calculate time for alarm
alarm_time = (current_time_hours + wait_time_hours) % 24

# Format and print output
print('Alarm will go off at ' + str(int(alarm_time)) + ' hundred hours')
