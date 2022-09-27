import sys

min_num = sys.maxsize

while True:
    curr_num = input()

    if curr_num != "Stop" and int(curr_num) < min_num:
        min_num = int(curr_num)

    if curr_num == "Stop":
        print(min_num)
        break



