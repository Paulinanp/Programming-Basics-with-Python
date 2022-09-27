screening_type = input()
rows = int(input())
cols = int(input())
price = 0

if screening_type == "Premiere":
    price = 12
elif screening_type == "Normal":
    price = 7.5
elif screening_type == "Discount":
    price = 5

print(f"{rows * cols * price:.2f} leva")