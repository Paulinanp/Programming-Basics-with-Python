from math import floor

name_series = input()
seasons_count = int(input())
episods_count = int(input())
time_episod = float(input())

time_ads = time_episod * 0.2
full_episode = time_ads + time_episod
special_episode = 10 * seasons_count

full_time = full_episode * episods_count * seasons_count + special_episode

print(f"Total time needed to watch the {name_series} series is {floor(full_time)} minutes.")