expenses = []
while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Show Total")
    print("4. Exit")
    print("5. Count Expenses")
    print("6. Delete Expense")
    choice =input("Enter command(1-6):")


    if choice == "1":
        expense = float(input("Enter expense amount: "))
        expenses.append(expense)
        print("Expense added successfully.")
    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            print("Expenses:")
            for expense in expenses:
                print(f"- ${expense:.2f}")
    elif choice == "3":
        total = sum(expenses)
        print(f"Total Expenses: ${total:.2f}")
    elif choice == "4":
        print("Good Bye")
        break
    elif choice =="5":
        print(f"Number of expenses recorded: {len(expenses)}")
    elif choice == "6":
        if len(expenses) == 0:
            print("No expenses to delete.")
        else:
            index = int(input("Enter the index of the expense to delete: ")) - 1
            if 0 <= index < len(expenses):
                deleted_expense = expenses.pop(index)
                print(f"Expense deleted: ${deleted_expense:.2f}")
            else:
                print("Invalid index.")
    else:
        print("Invalid command. Please try again.")