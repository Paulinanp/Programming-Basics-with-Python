bitcoin_count = int(input())
china_yune_count = float(input())
commision = float(input())

dolar = 1.76
euro = 1.95
bitcoin_price_leva = bitcoin_count * 1168
china_yune_price_dolar = china_yune_count * 0.15
china_yune_price_leva = china_yune_price_dolar * 1.76

price_euro = (bitcoin_price_leva + china_yune_price_leva) / 1.95

commision_price = price_euro * (commision/100)
final_sum = price_euro - commision_price

print(f"{final_sum:.2f}")

