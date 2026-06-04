import json
FILE_NAME="expenses.json"
def load_expenses():
    try:
        with open(FILE_NAME,"r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
def save_expenses(expenses):
    with open(FILE_NAME,"w") as file:
        json.dump(expenses,file,indent=2)
def add_expenses(category,amount):
    expenses=load_expenses()
    expense={
        "category":category,
        "amount":amount
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("expense added successfully")


def get_summary():
    expenses=load_expenses()
    summary={}
    for expense in expenses:
        category =expense["category"]
        amount= expense["amount"]
    if category in summary:
        summary[category]+=amount
    else:
        summary[category]=amount
    print("\nExpenses summary")
    for category,total in summary.items():
     print(f"{category}: {total}")


def view_all():
    expenses=load_expenses()
    if not expenses:
        print("no expenses found")
        return
    print("\n All expenses")
    for expense in expenses:
        print(f"category:{expense['category']}, amount:{expense['amount']}")
        
