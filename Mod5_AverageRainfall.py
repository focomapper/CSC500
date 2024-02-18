import calendar

# Initialize variables
num_years = 0
num_months = 0
total_rain = 0

# Get user input for number of years
try:
    num_years = int(input("Enter number of years: "))
except ValueError:
    print("Number of years must be a whole number. Run program again and enter valid number of years")
    exit()

# Outer loop through number of years
for y in range(num_years):
    print(f"Year: {y + 1}")
    
    # Inner loop through months in year
    for m in range(12):  # Loop through 12 times, one for each month in year
        try:  # Ensure inches are float
            inches_rain = float(input(f"Enter the inches of rain for month {calendar.month_name[m+1]}: "))
            num_months += 1
            total_rain += inches_rain
        except ValueError:
            print("Your input for inches of rain was not a number, run program again and enter valid inches")
            exit()

# Calculate average rain per month
average_rain = round(total_rain/num_months, 2)

# Print required output
print(f"\nTotal number of months: {num_months}")
print(f"Total inches of rain: {round(total_rain, 2)} inches")
print(f"Average rainfall per month for period of {num_years} years: {average_rain} inches")
