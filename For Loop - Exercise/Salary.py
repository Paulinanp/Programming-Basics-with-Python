tabs_count = int(input())
salary = int(input())

money_lost = 0

for i in range(1, tabs_count + 1):
    tab = input()

    if tab == "Facebook":
        money_lost = 150
        salary -= money_lost
    elif tab == "Instagram":
        money_lost = 100
        salary -= money_lost
    elif tab == "Reddit":
        money_lost = 50
        salary -= money_lost

    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(salary)


