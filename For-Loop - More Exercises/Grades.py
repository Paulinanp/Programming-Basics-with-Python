students_cnt = int(input())

average = 0
fail_cnt = 0
good_cnt = 0
very_good_cnt = 0
top_std_cnt = 0

for i in range(students_cnt):
    grade_of_student = float(input())
    average += grade_of_student

    if 2 <= grade_of_student < 3:
        fail_cnt += 1
    elif 3 <= grade_of_student <= 3.99:
        good_cnt += 1
    elif 4 <= grade_of_student <= 4.99:
        very_good_cnt += 1
    elif grade_of_student >= 5:
        top_std_cnt += 1

top_std_per = top_std_cnt / students_cnt * 100
very_good_per = very_good_cnt / students_cnt * 100
good_per = good_cnt / students_cnt * 100
fail_per = fail_cnt / students_cnt * 100

print(f"Top students: {top_std_per:.2f}% \nBetween 4.00 and 4.99: {very_good_per:.2f}%"
      f"\nBetween 3.00 and 3.99: {good_per:.2f}% \nFail: {fail_per:.2f}%")
print(f"Average: {(average / students_cnt):.2f}")