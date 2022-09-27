capacity_of_stadion = int(input())
fans_cnt = int(input())

sector_A_cnt = 0
sector_B_cnt = 0
sector_V_cnt = 0
sector_G_cnt = 0

for sectors in range(fans_cnt):
    sector = input()

    if sector == 'A':
        sector_A_cnt += 1
    elif sector == 'B':
        sector_B_cnt += 1
    elif sector == 'V':
        sector_V_cnt += 1
    elif sector == 'G':
        sector_G_cnt += 1

sector_A_per = sector_A_cnt / fans_cnt * 100
sector_B_per = sector_B_cnt / fans_cnt * 100
sector_V_per = sector_V_cnt / fans_cnt * 100
sector_G_per = sector_G_cnt / fans_cnt * 100
percent_fans = fans_cnt / capacity_of_stadion * 100

print(f'{sector_A_per:.2f}%')
print(f'{sector_B_per:.2f}%')
print(f'{sector_V_per:.2f}%')
print(f'{sector_G_per:.2f}%')
print(f'{percent_fans:.2f}%')
