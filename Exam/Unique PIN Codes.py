upper_first_num = int(input())
upper_second_num = int(input())
upper_third_num = int(input())

prime_nums = [2, 3, 5, 7, 13]

for i in range(1, upper_first_num + 1):
    for j in range(1 , upper_second_num + 1):
        for k in range(1, upper_third_num + 1):
            if i % 2 == 0 and k % 2 == 0 and j in prime_nums:
                print(f"{i} {j} {k}")

