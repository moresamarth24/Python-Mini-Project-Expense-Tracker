expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    expenses.append((name, amount))
    print("✅ Expense added")

def view_expenses():
    if not expenses:
        print("📭 No expenses recorded")
    else:
        print("\n📊 Expense List")
        for i, (name, amount) in enumerate(expenses, 1):
            print(f"{i}. {name} - ₹{amount}")

def total_expense():
    total = sum(amount for _, amount in expenses)
    print(f"\n💰 Total Spending: ₹{total}")

def expense_menu():
    while True:
        print("\n----- EXPENSE TRACKER MENU -----")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spending")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            print("👋 Exiting Expense Tracker")
            break
        else:
            print("❌ Invalid choice")

expense_menu()
