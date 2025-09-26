print("Welcome to the tip calculator!")  # Welcome message

# Get user inputs
bill = float(input("What was the total bill? $"))  # Total bill amount
tip = int(input("What percentage tip would you like to give? 10 12 15 "))  # Tip %
people = int(input("How many people to split the bill? "))  # Number of people

# Calculate the tip and total per person
tipPercent = tip / 100  # Convert tip to decimal
totalTip = bill * tipPercent  # Tip amount
totalBill = bill + totalTip  # Total bill including tip
perPerson = totalBill / people  # Amount each person should pay
finalAmount = round(perPerson, 2)  # Round to 2 decimal places

# Output the result
print(f"Each person should pay: ${finalAmount}")
