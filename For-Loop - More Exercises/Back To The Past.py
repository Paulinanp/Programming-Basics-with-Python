money = float(input())
year_that_should_live = int(input())

years_old = 18

for year in range(1800, year_that_should_live + 1):
    if year % 2 == 0:
        money = money - 12000
    else:
        money = money - (years_old * 50 + 12000)

    years_old += 1

if money < 0:
    print(f"He will need {abs(money):.2f} dollars to survive.")
else:
    print(f"Yes! He will live a carefree life and "
          f"will have {money:.2f} dollars left.")


