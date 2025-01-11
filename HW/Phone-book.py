phone_book = {}

while True:
    # add a number
    print()
    while True:
        q = input("Add new contact?(yes/no)_")
        if "y" in q or "Y" in q:
            new_name = input("Name here_")
            new_number = input("Number here_")
            if new_name.casefold() in phone_book.keys():
                print("!The name is already exist")
                print(phone_book[new_name])
            else:
                phone_book[new_name] = new_number
        else:
            break
    # delete a number
    q = input("Delete contact?(yes/no)_")
    if "y" in q or "Y" in q:
        del_name = input("Name to delete here_")
        if del_name.casefold() in phone_book.keys():
            print(f"The contact {del_name} : {phone_book.pop(del_name)} was deleted.")
        else:
            print("!The name is not in the list")
    # refactor a number
    q = input("Edit contact?(yes/no)_")
    if "y" in q or "Y" in q:
        edit_name = input("Name to edit here_")
        new_name = input("New name here_")
        new_number = input("New number here_")
        if edit_name.casefold() in phone_book.keys():
            phone_book[edit_name] = new_name
            phone_book[new_name] = new_number
        else:
            print("!The name is not in the list")
    # show all numbers
    q = input("Show contacts?(yes/no)_")
    if "y" in q or "Y" in q:
        n = 1
        print("Contacts:")
        for i,j in phone_book.items():
            name = f"{n}) {i} "
            print(name, " "*(15-len(name)), f": {j}")
            n += 1
    q = input("Close the program?(yes/no)_")
    if "y" in q or "Y" in q:
        break
