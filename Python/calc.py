num1 = float(input("Give me a number: "))
op = input("Enter an operator: ")
num2 = float(input("Give me another number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "x":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid operator please chose one of the following, +, -, x, /, ")


