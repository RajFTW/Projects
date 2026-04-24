expenses = []

while True:
    print("-" * 50)
    print("-:Welcome to Expense Tracker:-\n\tPlease select one of the following options!")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Category Summary")
    print("5. Delete Expense")
    print("6. Exit")

    # Choice input
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Enter a number.")
        continue

    # 1. Add Expense
    if choice == 1:
        print("-" * 50)
        name = input("Enter expense name: ").strip()

        if name == "":
            print("Name cannot be empty!")
            continue

        try:
            amount = int(input("Enter amount: "))
        except ValueError:
            print("Invalid amount!")
            continue

        expenses.append({"name": name, "amount": amount})
        print("Expense added successfully!")

    # 2. View Expenses
    elif choice == 2:
        print("-" * 50)

        if not expenses:
            print("No expenses available!")
        else:
            for i, exp in enumerate(expenses, start=1):
                print(f"{i}. {exp['name']} - ${exp['amount']}")

    # 3. Total Expense
    elif choice == 3:
        print("-" * 50)

        if not expenses:
            print("No expenses available!")
        else:
            total = sum(exp["amount"] for exp in expenses)
            print(f"Total Expenses: ${total}")

    # 4. Category Summary
    elif choice == 4:
        print("-" * 50)

        if not expenses:
            print("No expenses available!")
            continue

        summary = {}

        for exp in expenses:
            name = exp["name"]
            amount = exp["amount"]

            if name in summary:
                summary[name] += amount
            else:
                summary[name] = amount

        print("Category Summary:")
        for category, total in summary.items():
            print(f"{category}: ${total}")

    # 5. Delete Expense
    elif choice == 5:
        print("-" * 50)

        if not expenses:
            print("No expenses to delete!")
            continue

        for i, exp in enumerate(expenses, start=1):
            print(f"{i}. {exp['name']} - ${exp['amount']}")

        try:
            index = int(input("Enter expense number to delete: "))
            if 1 <= index <= len(expenses):
                deleted = expenses.pop(index - 1)
                print(f"Deleted: {deleted['name']} - ${deleted['amount']}")
            else:
                print("Invalid index!")
        except ValueError:
            print("Invalid input!")

    # 6. Exit
    elif choice == 6:
        print("-" * 50)
        print("Thank you for using Expense Tracker!")
        print("-" * 50)
        break

    else:
        print("Invalid choice! Please try again.")