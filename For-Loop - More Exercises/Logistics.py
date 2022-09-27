load_cnt = int(input())
total_ton = 0

truck_cnt = 0
train_cnt = 0
minibus_cnt = 0

for i in range(load_cnt):
    load_ton = int(input())
    total_ton += load_ton

    if load_ton <= 3:
        minibus_cnt += load_ton

    if 3 < load_ton <= 11:
        truck_cnt += load_ton

    if load_ton > 11:
        train_cnt += load_ton

final_price = (minibus_cnt * 200 + truck_cnt * 175 + train_cnt * 120) / total_ton

print(f"{final_price:.2f}")

minibus_percent = (minibus_cnt / total_ton) * 100
truck_percent = truck_cnt / total_ton * 100
train_percent = train_cnt / total_ton * 100

print(f"{minibus_percent:.2f}%")
print(f"{truck_percent:.2f}%")
print(f"{train_percent:.2f}%")

