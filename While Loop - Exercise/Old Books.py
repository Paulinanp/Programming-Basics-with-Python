favourite_book = input()
counter = 0
flag = True

book_input = input()

while book_input != favourite_book:
    book_input = input()
    counter += 1

    if book_input == "No More Books":
        flag = False
        print("The book you search is not here!")
        print(f"You checked {counter} books.")
        break

if flag:
    print(f"You checked {counter} books and found it.")

