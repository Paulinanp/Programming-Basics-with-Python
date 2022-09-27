minutes_walking = int(input())
walkings_count = int(input())
calories = float(input())

total_burning_calories = walkings_count * minutes_walking * 5

if total_burning_calories >= calories * 0.5:
    print(f"Yes, the walk for your cat is enough. "
          f"Burned calories per day: {total_burning_calories}.")
else:
    print(f"No, the walk for your cat is not enough."
          f" Burned calories per day: {total_burning_calories}.")