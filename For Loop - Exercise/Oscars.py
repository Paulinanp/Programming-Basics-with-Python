name_of_actor = input()
poins_from_academy = float(input())
count_graders = int(input())

score = 0

for i in range(1, count_graders + 1):
    name_of_grader = input()
    point = float(input())

    if score == 0:
        final_points = poins_from_academy + (len(name_of_grader) * point) / 2
    else:
        final_points = score + (len(name_of_grader) * point) / 2

    score = final_points

    if score > 1250.5:
        print(f"Congratulations, "
              f"{name_of_actor} got a nominee for leading role with {score:.1f}!")
        break

if score <= 1250.5:
    need_poins = 1250.5 - score
    print(f"Sorry, {name_of_actor} you need {need_poins:.1f} more!")