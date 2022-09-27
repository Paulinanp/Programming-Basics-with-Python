text = input()

fruits = ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"]
vegetables = ["tomato", "cucumber", "pepper", "carrot"]

if text in fruits:
    print("fruit")
elif text in vegetables:
    print("vegetable")
else:
    print("unknown")