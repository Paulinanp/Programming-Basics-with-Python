name_film = input()
days_count = int(input())
tickets_count = int(input())
tickets_price = float(input())
percent_per_cinema = int(input())

price_tickets_per_day = tickets_price * tickets_count
price_for_all_days = days_count * price_tickets_per_day

money_for_cinema = price_for_all_days * percent_per_cinema / 100

final_sum = price_for_all_days - money_for_cinema

print(f"The profit from the movie {name_film} is {final_sum:.2f} lv.")