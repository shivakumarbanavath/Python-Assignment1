# Task 1: Perform Basic Mathematical Operations
num1=float(input("Enter the first Number: "))
num2=float(input("Enter the second Number: "))
addition=num1+num2
subtraction=num1-num2
multiplication=num1*num2
if num2 != 0:
    division=num1/num2
else:
    division= ("Cannot divide by zero"  )
print()
print("Addition",addition)
print("Subtraction",subtraction)
print("Multiplication",multiplication)
print("Division",division)