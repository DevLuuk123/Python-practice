# Made by Luuk Klingens
# GitHub: https://github.com/devluuk123
# Copyright 2025

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 == 0:
        result = "Error: division by zero"
    else:
        result = num1 / num2
else:
    result = "Invalid operator"

print("Result:", result)