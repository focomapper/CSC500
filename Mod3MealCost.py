# Initialize meal list
meal = [0, 0.18, 0.07]

# Get price of meal from user and validate that it's a number
try:
    meal[0] = (float(input("Enter the price of meal: ")))
except ValueError:
    print("Your input was not a number, run program again and enter valid number")
    exit()

# Check that cost is greater than 0, no free meals at this establishment
if not meal[0] > 0:
    print("Your input must be greater than 0, run program again and enter valid number")
    exit()

# Calculate total meal cost
total_cost = meal[0] + (meal[0] * meal[1]) + (meal[0] * meal[2])

# Output results with formatting
print('Total tip is: ' + '${:,.2f}'.format(meal[0] * meal[1]))
print('Total tax is: ' + '${:,.2f}'.format(meal[0] * meal[2]))
print('Total meal cost is: ' + '${:,.2f}'.format(total_cost))
