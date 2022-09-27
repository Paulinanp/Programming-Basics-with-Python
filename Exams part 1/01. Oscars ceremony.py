rent_hall = int(input())

statuette = rent_hall - (rent_hall * 0.3)
catering = statuette - (statuette * 0.15)
sound = catering / 2

final_sum = statuette + catering + sound + rent_hall

print(f"{final_sum:.2f}")