

# Define a list of month names where the index corresponds to the month number - 1
month_names = ["January", "February", "March", "April", "May", "June", 
               "July", "August", "September", "October", "November", "December"]

# Prompt the user to enter a month number
month_number = int(input("Enter the month (1-12): "))  # Corrected: added parentheses around input()

# Check if the entered number is within the valid range
if 1 <= month_number <= 12:
    # Get the corresponding month name from the list
    month_name = month_names[month_number - 1]
    # Output the result
    print(f"Month {month_number} is {month_name}")
else:
    # Output an error message for invalid input
    print("Error: Please enter a number between 1 and 12.")
