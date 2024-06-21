monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your monthly expenses: ")
monthly_income = float(monthly_income)
monthly_expenses = float(monthly_expenses)
monthly_savings = monthly_income - monthly_expenses
projected_saving = (monthly_savings*12) + (monthly_savings*12*0.05)
projected_saving = float(projected_saving)
print("Your monthly savings are:", "$",monthly_savings,".")
print("Projected savings after one year, with interest, is:", "$",projected_saving,".")