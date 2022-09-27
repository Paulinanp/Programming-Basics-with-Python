count_not_good_grade = int(input())
counter = 0
numbers_of_problems = 0
average_score = 0
last_problem = " "
flag = True

while counter < count_not_good_grade:
    name_of_ex = input()
    if name_of_ex == "Enough":
        flag = False
        break

    grade = int(input())
    if grade <= 4:
        counter += 1
    average_score += grade
    numbers_of_problems += 1
    last_problem = name_of_ex

if not flag:
    print(f"Average score: {average_score / numbers_of_problems:.2f}")
    print(f"Number of problems: {numbers_of_problems}")
    print(f"Last problem: {last_problem}")
else:
    print(f"You need a break, {counter} poor grades.")

