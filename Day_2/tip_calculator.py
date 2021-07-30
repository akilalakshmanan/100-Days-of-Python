print("Welcome to the tip calculator \n")
bill = float(input("What was the total bill $? \n"))
tip = int(input("What percentage of tip would you like to give? 10, 12 or 15? \n"))
people_split_bill = int(input("How many people to split the bill? \n"))

total_tip = bill * (tip / 100)
#print("The total tip to be given is " + str(total_tip) + "\n")

total_bill = bill + total_tip
#print("Your total bill amounts to " + str(total_bill) + "\n")

final_split_bill = round(total_bill/people_split_bill, 2)

print("Each person should pay: $" + str(final_split_bill))
