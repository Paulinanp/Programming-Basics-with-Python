total_balance = 0

while True:
    current_sum = input()

    if current_sum != "NoMoreMoney" and float(current_sum) < 0:
        print("Invalid operation!")
        print(f"Total: {total_balance:.2f}")
        break

    if current_sum != "NoMoreMoney":
        total_balance += float(current_sum)

    if str(current_sum) == "NoMoreMoney":
        print(f"Total: {total_balance:.2f}")
        break

    print(f"Increase: {float(current_sum):.2f}")



