time_shoot = int(input())
scene_count = int(input())
scene_time = int(input())

ground_prepering = time_shoot * 0.15
time_for_scenes = scene_time * scene_count

total_time = ground_prepering + time_for_scenes

if time_shoot < total_time:
    time_need = total_time - time_shoot
    print(f"Time is up! To complete the movie you need {round(time_need)} minutes.")
else:
    time_left = time_shoot - total_time
    print(f"You managed to finish the movie on time! You have {round(time_left)} minutes left!")