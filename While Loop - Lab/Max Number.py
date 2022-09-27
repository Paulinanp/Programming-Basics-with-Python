import sys

max_num = -sys.maxsize

while True:
    curr_num = input()

    if curr_num != "Stop" and int(curr_num) > max_num:
        max_num = int(curr_num)

    if curr_num == "Stop":
        print(max_num)
        break



