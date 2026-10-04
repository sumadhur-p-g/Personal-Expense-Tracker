print("==========================================")
print("          PERSONAL EXPENSE TRACKER")
print("==========================================")


def save_expenses(expenses):
    file = open("expenses.txt", "w")

    for expense in expenses:
        file.write(expense[0] + "\n")
        file.write(str(expense[1]) + "\n")
        file.write(expense[2] + "\n")

    file.close()


def load_expenses():
    expenses = []

    try:
        file = open("expenses.txt", "r")

        while True:
            date = file.readline()

            if date == "":
                break

            date = date.strip()
            amount = float(file.readline())
            category = file.readline().strip()

            expense = [date, amount, category ]
            expenses.append(expense)

        file.close()

    except FileNotFoundError:
        pass

    return expenses



expenses = load_expenses()


while True:

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expense")
    print("4. Category Summary")
    print("5. Check Budget")
    print("6. Edit Expense")
    print("7. Delete Expense")
    print("8. Exit")
    choice = int(input("\nEnter your choice: "))

    if choice == 1:

        date = input("Enter date (DD-MM-YYYY): ")
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        

        expense = [date, amount, category]
        expenses.append(expense)

        save_expenses(expenses)

        print("\nExpense added successfully!")

    
    

    elif choice == 2:

        print("\n============================== EXPENSE LIST ==============================")

        if len(expenses) == 0:
            print("No expenses available.")

        else:
            print("{:<5} {:<15} {:<12} {:<15}".format(
                 "No.", "Date", "Amount", "Category"
            ))

            print("-" * 72)

            for i in range(len(expenses)):
                print("{:<5} {:<15} {:<12.2f} {:<15}".format(
                  i + 1,
                  expenses[i][0],
                  expenses[i][1],
                  expenses[i][2]
            ))

            print("-" * 72)


    elif choice == 3:

        total = 0

        for expense in expenses:
            total = total + expense[1]

        print("\nTotal Expense:", total)
        
    elif choice == 4:

        category_totals = {}

        for expense in expenses:

            category = expense[2]
            amount = expense[1]

            if category in category_totals:
                category_totals[category] = category_totals[category] + amount
            else:
                category_totals[category] = amount

        print("\n========== CATEGORY SUMMARY ==========")

        if len(category_totals) == 0:
            print("No expenses available.")

        else:
            for category in category_totals:
                print(category, ":", category_totals[category])
                
    elif choice == 5:

        budget = float(input("\nEnter your monthly budget: "))

        total = 0

        for expense in expenses:
            total = total + expense[1]

        print("\nTotal Expense:", total)
        print("Budget:", budget)

        if total > budget:
            print("Status: Budget exceeded!")
            print("Amount exceeded:", total - budget)

        else:
            print("Status: Within budget.")
            print("Amount remaining:", budget - total)
            
            
    elif choice == 6:

        if len(expenses) == 0:
            print("\nNo expenses available.")

        else:
            print("\n========== EXPENSES ==========")

            for i in range(len(expenses)):
                print("\nExpense", i + 1)
                print("Date:", expenses[i][0])
                print("Amount:", expenses[i][1])
                print("Category:", expenses[i][2])
                

            number = int(input("\nEnter expense number to edit: "))

            if number >= 1 and number <= len(expenses):

                index = number - 1

                print("\nEnter new details:")

                expenses[index][0] = input("Enter new date (DD-MM-YYYY): ")
                expenses[index][1] = float(input("Enter new amount: "))
                expenses[index][2] = input("Enter new category: ")
                

                save_expenses(expenses)

                print("\nExpense updated successfully!")

            else:
                print("\nInvalid expense number.")
            
    elif choice == 7:

        if len(expenses) == 0:
            print("\nNo expenses available.")

        else:
            print("\n========== EXPENSES ==========")

            for i in range(len(expenses)):
                print("\nExpense", i + 1)
                print("Date:", expenses[i][0])
                print("Amount:", expenses[i][1])
                print("Category:", expenses[i][2])
                

            number = int(input("\nEnter expense number to delete: "))

            if number >= 1 and number <= len(expenses):

                expenses.pop(number - 1)

                save_expenses(expenses)

                print("\nExpense deleted successfully!")

            else:
                print("\nInvalid expense number.")

    elif choice == 8:

        print("\nThank you for using Personal Expense Tracker!")
        break

    else:

        print("\nInvalid choice!")