groups_count = int(input())

total_people = 0
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0

for i in range(1, groups_count + 1):
    people_in_group = int(input())

    if people_in_group <= 5:
        musala += people_in_group
    elif people_in_group <= 12:
        monblan += people_in_group
    elif people_in_group <= 25:
        kilimandjaro += people_in_group
    elif people_in_group <= 40:
        k2 += people_in_group
    elif people_in_group > 40:
        everest += people_in_group

    total_people += people_in_group

musala_percent = musala / total_people * 100
monblan_percent = monblan / total_people * 100
kilimandjaro_percent = kilimandjaro / total_people * 100
k2_percent = k2 / total_people * 100
everest_percent = everest / total_people * 100

print(f"{musala_percent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kilimandjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")


