contacts={}
while True:
    print("1.add contact")
    print("2.search contact")
    print("3.update contact")
    print("4.delete contact")
    print("5.list all contact")
    print("6.exit")
    choice=input("enter choice:")
    if choice=="1":
        name=input("enter name: ")
        phone=input("enter number: ")
        contacts[name]=phone
        print("contact added")
    elif choice=="2":
        name=input("enter name: ")
        if name in contacts:
            print(contacts.get(name))
        else:
            print("not found")
    elif choice=="3":
        name=input("enter name: ")
        if name in contacts:
            phone=input("enter new number: ")
            contacts[name]=phone
            print("contact updated")
        else:
            print("contact not founded")
    elif choice=="4":
        name=input("enter name: ")
        if name in contacts:
            del contacts[name]
            print("contact deleted")
        else:
            print("contact not found")
    elif choice=="5":
        print(contacts)
    elif choice=="6":
        print("program ended")
        break
    else:
        print("invalid choice")
