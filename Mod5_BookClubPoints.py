# Initialize number of books, total points
num_books = 0
total_points = 0

# Get user input for number of books purchased
try:
    num_books = int(input("Enter number of books purchased this month: "))
except ValueError:
    print("Number of books must be a whole number. Run program again and enter valid number of books")

# Determine points based on number of books
if num_books < 4:
    total_points = 5
elif 4 <= num_books < 6:
    total_points = 15
elif 6 <= num_books < 8:
    total_points = 30
elif num_books >= 8:
    total_points = 60

# Output results
print(f"\nTotal points for {num_books} books = {total_points} points.")
