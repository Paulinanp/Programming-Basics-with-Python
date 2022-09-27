dancers_cnt = int(input())
points_cnt = float(input())
season = input()
place = input()

money = 0
costs = 0

if place == "Bulgaria":
    money = dancers_cnt * points_cnt

    if season == "summer":
        costs = money * 0.05
        money -= costs
    elif season == "winter":
        costs = money * 0.08
        money -= costs

elif place == "Abroad":
    money = dancers_cnt * points_cnt
    money += money * 0.5
    if season == "summer":
        costs = money * 0.1
        money -= costs
    elif season == "winter":
        costs = money * 0.15
        money -= costs

charity = money * 0.75
money_left = money - charity
money_per_dancer = money_left / dancers_cnt

print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")