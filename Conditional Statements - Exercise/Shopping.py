budget = float(input())
videoCards_count = int(input())
cpu_count = int(input())
ram_count = int(input())

discout = 0

price_video_card = 250 * videoCards_count
price_cpu = (price_video_card * 0.35)
price_ram = (price_video_card * 0.1)

total_price_cpu = cpu_count * price_cpu
total_price_ram = price_ram * ram_count

total_sum = price_video_card + total_price_cpu + total_price_ram

if videoCards_count > cpu_count:
    discout = total_sum * 0.15
    total_sum -= discout

if total_sum <= budget:
    moneyLeft = budget - total_sum
    print(f"You have {moneyLeft:.2f} leva left!")
else:
    moneyNeeded = total_sum - budget
    print(f"Not enough money! You need {moneyNeeded:.2f} leva more!")