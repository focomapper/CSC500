# Get price of meal from user and validate that it's a number
try:
    meal_cost = (float(input("Enter the price of meal: ")))
except ValueError:
    print("Your input was not a number, run program again and enter valid number")
    exit()

# Check that cost is greater than 0, no free meals at this establishment
if not meal_cost > 0:
    print("Your input must be greater than 0, run program again and enter valid number")
    exit()

# Calculate 18% tip and round to 2 decimals
tip = meal_cost * 0.18

# Calculate 7% sales tax and round to 2 decimals
tax = meal_cost * 0.07

# Calculate total meal cost
total_cost = meal_cost + tip + tax

# Output results with formatting
print('Total tip is: ' + '${:,.2f}'.format(tip))
print('Total tax is: ' + '${:,.2f}'.format(tax))
print('Total meal cost is: ' + '${:,.2f}'.format(total_cost))


