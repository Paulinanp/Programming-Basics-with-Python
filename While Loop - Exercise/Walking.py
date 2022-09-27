steps_cnt = 0

current_input = input()

while current_input != "Going home":
    steps = int(current_input)
    steps_cnt += steps

    if steps_cnt >= 10000:
        break

    current_input = input()

if current_input == "Going home":
    steps_home = int(input())
    steps_cnt += steps_home

if steps_cnt >= 10000:
    print("Goal reached! Good job!")
    print(f"{abs(steps_cnt - 10000)} steps over the goal!")
else:
    print(f"{abs(10000 - steps_cnt)} more steps to reach goal.")