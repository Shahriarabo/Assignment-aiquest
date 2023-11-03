contact = {}
def showcontact():
    print(contact.items())
    print("name \t Contest")
    for key in contact:
        print("{} \t {} ".format(key,contact.get(key)))


while True:
    choice = int(input("1. Create, the Contact : \n"
                   "2. Update the Contact : \n"
                   "3. Read the Contact : \n"
                   "4. Delete the Contact : \n"
                   "Please Enter the Number between 1 to 4 : "))

    if choice == 1:
        name = input(" Enter The Name : ")
        number = input("Enter The Number : ")
        contact[name]= number

    elif choice == 2:
        Update = input("which one Update The Contact : ")
        if Update in contact:
            name = input("Change Your Name : ")
            phone = input("Change Your Number : ")
            contact[Update] = name , phone
            print("The Contact Updated Successfully")
            showcontact()
        else:
            print("The Name is not Found")

    elif choice == 3:
        if not contact:
            print("The Contact is empty")
        else:
            showcontact()

    elif choice == 4:
        delete = input("Which Contact Do you want delete : ")
        if delete in contact:
            deletecon = input("Do you want to delete Contact [y/n] : ")
            if deletecon == "y" or deletecon == "Y":
                contact.pop(delete)
                print("The Contact Delete Successfully")
                showcontact()
        else:
            print("The Contact is not found")

    else:
        break
