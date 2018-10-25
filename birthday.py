dict = {}   #null dictionary so that we can store the data in form of key and value....
while 1:     #infinte loop
    print("============ BIRTHDAY REMINDER APP ============")
    print("1. VIEW BIRTHDAY....")
    print("2. ADD BIRTH DATE OF YOUR FRIEND...")
    print("3. EXIT")

    choice = int(input("CHOOSE ANY OPTION:::"))  #input returns in form of string but we have to compare choice by int...So, typecasting is used
    if choice == 1:
        if len(dict.keys()) == 0:
            print("NO DATA... PLEASE ADD BIRTH DATE ")
        else:
            name = input("ENTER THE NAME :::")
            birthday = dict.get(name, "NO DATA FOUND")
            print(birthday)
    elif choice == 2:
        name_1 = input("ENTER NAME TO ADD:::")
        date = input("ENTER THE BIRTH DATE:::")
        dict[name_1] = date
    elif choice == 3:
        break
    else:
        print("YOU HAVE CHOSEN A WRONG CHOICE")


