income = input("Enter your monthly income:")
expense = input("Enter your total monthly expense:")
saving = int(income) - int(expense)
projected_saving = saving * 12 + (saving * 12 * 0.05)
print("Your monthly savings are:", saving)
print("Projected savings after one year, with interest, is:", projected_saving)