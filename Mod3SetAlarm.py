# Initialize list
alarm_specs = [0, 0]

# Get time from user and validate that it's a whole number
try:
    alarm_specs[0] = (int(input("Enter time in hours: ")))
except ValueError:
    print("Your input was not a whole number (hours), run program again and enter valid number")
    exit()

# Make sure time entered is 23 or less
if not (23 > alarm_specs[0] >= 0):
    print("Your input must be from 0 to 23, run program again and enter valid time")
    exit()

# Get time to wait for alarm from user and validate that it's a number
try:
    alarm_specs[1] = (int(input("Enter hours to wait for alarm: ")))
except ValueError:
    print("Your input was not a number (hours), run program again and enter valid number")
    exit()

# Make sure alarm time is a positive number
if not (23 > alarm_specs[1] >= 0):
    print("Your input must be from greater than 0, run program again and enter valid time")
    exit()

# Calculate time for alarm
alarm_time = (alarm_specs[0] + alarm_specs[1]) % 24

# Format and print output
print('Alarm will go off at ' + str(int(alarm_time)) + ' hundred hours')
