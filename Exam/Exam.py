students_cnt = int(input())

fail_cnt = 0
good_cnt = 0
very_good_cnt = 0
top_std_cnt = 0
average = 0

for i in range(1, students_cnt + 1):
    grade = float(input())

    if 2 <= grade <= 2.99:
        fail_cnt += 1
    elif 3 <= grade <= 3.99:
        good_cnt += 1
    elif 4 <= grade <= 4.99:
        very_good_cnt += 1
    elif grade >= 5:
        top_std_cnt += 1

    average += grade

fail_per = fail_cnt / students_cnt * 100
good_per = good_cnt / students_cnt * 100
very_good_per = very_good_cnt / students_cnt * 100
top_std_per = top_std_cnt / students_cnt * 100

print(f"Top students: {top_std_per:.2f}%")
print(f"Between 4.00 and 4.99: {very_good_per:.2f}%")
print(f"Between 3.00 and 3.99: {good_per:.2f}%")
print(f"Fail: {fail_per:.2f}%")
print(f"Average: {(average/students_cnt):.2f}")