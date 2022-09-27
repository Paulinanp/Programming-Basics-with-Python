age = float(input())
gender = input()

output = " "

if gender == "m":
    if age >= 16:
      output = "Mr."
    else:
        output = "Master"
elif gender == "f":
    if age >= 16:
      output = "Ms."
    else:
        output = "Miss"

print(output)