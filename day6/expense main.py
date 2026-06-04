from expenses_utils import add_expenses,get_summary,view_all
while True:
    print("\n1. Add expense")
    print("\n2. Summary")
    print("\n.3 View all")
    print("\n.4 Exit")
    choice=input("enter choice: ")

    if choice=="1":
        category=input("enter category: ")
        amount=float(input("Enter amount: "))
        add_expenses(category,amount)
    elif choice=="2":
        get_summary()
    elif choice=="3":
        view_all()
    elif choice=="4":
        print("goodbye")
        break
    else:
        print("invald choice")