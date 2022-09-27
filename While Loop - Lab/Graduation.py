name_of_student = input()

count_fails = 0
average = 0
clas = 1

while clas <= 12:
    grade = float(input())

    if grade < 4:
        count_fails += 1
        if count_fails > 1:
            print(f"{name_of_student} has been excluded at {clas} grade")
            break

    elif grade >= 4:
        average += grade
        clas += 1

clas -= 1
if clas == 12:
    print(f"{name_of_student} graduated. Average grade: {(average / clas):.2f}")
