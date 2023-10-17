print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
math_symbol = input("Enter choice (1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if math_symbol == '1':
    print(num1 + num2)
elif math_symbol == '2':
    print(num1 - num2)
elif math_symbol == '3':
    print(num1 * num2)
elif math_symbol == '4': 
    print(num1 / num2)
else:
    print("Invalid input")