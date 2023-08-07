#TIP CALCULATOR
print("Welcome to the tip calculator.")
total_bill=float(input("What was the total bill? $"))
tip=int(input("What percentage tip would you like to give? 10, 12, 15: "))
NumPeople=int(input("How many people to split the bill with? "))
percentage=(tip+100)/100

bill=(total_bill*percentage)/NumPeople
print(f"Per Head Bill is: ${bill:.2f}")