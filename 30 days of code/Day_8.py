n = int(input("Number of entries in the phone book:"))
name_numbers = [input("Name and phone:").split(" ") for i in range(n)]
phone_book = {key:value for key, value in name_numbers}
while True:
    try:
        name = input("Name to look up:")
        if name in phone_book:
            print(("{} = {}").format(name, phone_book[name]))
        else:
            print("Not found")
    except:
        break
