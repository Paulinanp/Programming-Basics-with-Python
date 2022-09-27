num1 = int(input())
num2 = int(input())
operator = input()

value = 0

if operator == '+':
    value = num1 + num2
    if value % 2 == 0:
        print(f"{num1} {operator} {num2} = {value} - even")
    else:
        print(f"{num1} {operator} {num2} = {value} - odd")
elif operator == '-':
    value = num1 - num2
    if value % 2 == 0:
        print(f"{num1} {operator} {num2} = {value} - even")
    else:
        print(f"{num1} {operator} {num2} = {value} - odd")
elif operator == '*':
    value = num1 * num2
    if value % 2 == 0:
        print(f"{num1} {operator} {num2} = {value} - even")
    else:
        print(f"{num1} {operator} {num2} = {value} - odd")
elif operator == '/':
    if num2 == 0:
        print(f'Cannot divide {num1} by zero')
    else:
        print(f"{num1} {operator} {num2} = {num1 / num2:.2f}")
elif operator == '%':
    if num2 == 0:
        print(f'Cannot divide {num1} by zero')
    else:
        print(f"{num1} {operator} {num2} = {num1 % num2}")