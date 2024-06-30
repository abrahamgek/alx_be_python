num1 = input("Enter the first number:")
num2 = input("Enter the second number:")
num1 = float(num1)
num2 = float(num2)
operation = input("Choose the opertation (+, -, *, /):")
match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "undefined (cannot divide by zero)"
    case _:
        result = "Invalid operation selected"

# Output the result
print(f"The result is {result}")