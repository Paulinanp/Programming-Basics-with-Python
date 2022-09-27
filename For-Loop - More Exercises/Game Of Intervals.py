total_turns = int(input())

points = 0

from_0_to_9_cnt = 0
from_10_to_19_cnt = 0
from_20_to_29_cnt = 0
from_30_to_39_cnt = 0
from_40_to_50_cnt = 0
invalid_nums_cnt = 0

for turn in range(total_turns):
    number_inp = int(input())

    if 0 <= number_inp <= 9:
        points += number_inp * 0.2
        from_0_to_9_cnt += 1
    elif 10 <= number_inp <= 19:
        points += number_inp * 0.3
        from_10_to_19_cnt += 1
    elif 20 <= number_inp <= 29:
        points += number_inp * 0.4
        from_20_to_29_cnt += 1
    elif 30 <= number_inp <= 39:
        points += 50
        from_30_to_39_cnt += 1
    elif 40 <= number_inp <= 50:
        points += 100
        from_40_to_50_cnt += 1
    else:
        points /= 2
        invalid_nums_cnt += 1

from_0_to_9_per = from_0_to_9_cnt / total_turns * 100
from_10_to_19_per = from_10_to_19_cnt / total_turns * 100
from_20_to_29_per = from_20_to_29_cnt / total_turns * 100
from_30_to_39_per = from_30_to_39_cnt / total_turns * 100
from_40_to_50_per = from_40_to_50_cnt / total_turns * 100
invalid_nums_per = invalid_nums_cnt / total_turns * 100

print(f"{points:.2f}")
print(f"From 0 to 9: {from_0_to_9_per:.2f}%")
print(f"From 10 to 19: {from_10_to_19_per:.2f}%")
print(f"From 20 to 29: {from_20_to_29_per:.2f}%")
print(f"From 30 to 39: {from_30_to_39_per:.2f}%")
print(f"From 40 to 50: {from_40_to_50_per:.2f}%")
print(f"Invalid numbers: {invalid_nums_per:.2f}%")
