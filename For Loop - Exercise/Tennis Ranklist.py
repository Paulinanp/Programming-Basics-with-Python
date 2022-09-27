from math import floor

tournament_count = int(input())
started_points = int(input())

points = 0
final_points = 0
average_points = 0
percent_wins = 0
wins_count = 0

for i in range(1, tournament_count + 1):
    position = input()

    if position == "W":
        wins_count += 1
        points = 2000
        percent_wins = wins_count / tournament_count * 100
    elif position == "F":
        points = 1200
    elif position == "SF":
        points = 720

    if i < 2:
        final_points += points + started_points
    else:
        final_points += points

    average_points += points / tournament_count

print(f"Final points: {final_points}")
print(f"Average points: {floor(average_points)}")
print(f"{percent_wins:.2f}%")