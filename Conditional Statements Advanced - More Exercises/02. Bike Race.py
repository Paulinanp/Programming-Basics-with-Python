juniors_count = int(input())
seniors_count = int(input())
layout = input()

tax_juniors = 0
tax_seniors = 0

if  layout == "trail":
    tax_juniors = 5.5
    tax_seniors = 7
elif layout == "cross-country":
    tax_juniors = 8
    tax_seniors = 9.5
elif layout == "downhill":
    tax_juniors = 12.25
    tax_seniors = 13.75
elif layout == "road":
    tax_juniors = 20
    tax_seniors = 21.5

if juniors_count + seniors_count >= 50 and layout == "cross-country":
    tax_juniors -= tax_juniors * 0.25
    tax_seniors -= tax_seniors * 0.25

final_sum = (juniors_count * tax_juniors) + (seniors_count * tax_seniors)
costs = final_sum * 0.05
final_sum -= costs

print(f"{final_sum:.2f}")