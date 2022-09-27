cpu_price = float(input())
video_card_price = float(input())
ram_price = float(input())
ram_cnt = int(input())
discount = float(input())

cpu_price_lv = cpu_price * 1.57
video_card_price_lv = video_card_price * 1.57
ram_price_lv = (ram_price * ram_cnt) * 1.57

cpu_price_lv -= cpu_price_lv * discount
video_card_price_lv -= video_card_price_lv * discount

total_sum = cpu_price_lv + video_card_price_lv + ram_price_lv

print(f"Money needed - {total_sum:.2f} leva.")