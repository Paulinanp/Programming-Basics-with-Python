rent_hall = float(input())

cake = rent_hall * 0.2
drinks = cake - (cake * 0.45)
animator = rent_hall * 1/3

budget = rent_hall + cake + drinks + animator

print(budget)