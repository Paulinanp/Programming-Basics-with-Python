name_of_best_player = ''
goals_of_best_player = 0
hat_trick = False

while True:
    name_of_player = input()

    if name_of_player == "END":
        break

    curr_number_of_goals = int(input())

    if curr_number_of_goals > goals_of_best_player:
        goals_of_best_player = curr_number_of_goals
        name_of_best_player = name_of_player

        if curr_number_of_goals >= 3:
            hat_trick = True

            if curr_number_of_goals >= 10:
                break

print(f"{name_of_best_player} is the best player!")

if hat_trick:
    print(f"He has scored {goals_of_best_player} goals and made a hat-trick !!!")
else:
    print(f"He has scored {goals_of_best_player} goals.")