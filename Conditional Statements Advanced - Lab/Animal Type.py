animal = input()

is_reptile = ['crocodile', 'tortoise', 'snake']

if animal == "dog":
    print("mammal")
elif animal in is_reptile:
    print("reptile")
else:
    print("unknown")