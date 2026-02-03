#Tip calculator

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
total_amount = (bill+(bill*(tip/100)))
amount_to_be_paid_by_each_person = round(total_amount/people, 2)
print(f"Each person should pay: {amount_to_be_paid_by_each_person}")
