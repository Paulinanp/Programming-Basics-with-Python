agnecy = input()
tickets_for_adults = int(input())
tickets_for_kids = int(input())
price_for_adults = float(input())
tax = float(input())

all_tickets_for_adults = tickets_for_adults * price_for_adults + tickets_for_adults * tax
price_for_kids = price_for_adults - (price_for_adults * 0.7)
all_tickets_for_kids = price_for_kids * tickets_for_kids + tickets_for_kids * tax

final_price = all_tickets_for_kids + all_tickets_for_adults
money_for_agency = final_price * 0.2

print(f"The profit of your agency from {agnecy}"
      f" tickets is {money_for_agency:.2f} lv.")