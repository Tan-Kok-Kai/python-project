from Transactions import Transaction
from QuickOverview import QuickOverview
from Data_Dynamic import ExpenseAnalysis
from Category import Category
from Budget import Budget

def main():
    print("Welcome to the Expense Tracker!")

    print(f"Hello! What would you like to do")
    overview = QuickOverview("datagen_new.xlsx")
    result = overview.get_current_month_overview()
    print("Financial Overview for the Current Month:")
    print(f"- Total Budget: ${result['Total Budget']:.2f}")
    print(f"- Total Expense Spent: ${result['Total Expense']:.2f}")
    print(f"- Remaining Budget: ${result['Remaining Budget']:.2f}")
    
    while True:
        # Menu options
        print("\nMenu:")
        print("1. Manage Budget")
        print("2. Add Transaction")
        print("3. Others")
        print("0. Quit")

        choice = input("Enter your choice: ")
        print()

        if choice == "1":
            # Manage Budget
            print("What would you like to do?")
            while True:
                print("1. View Budget")
                print("2. Add Budget")
                print("3. Update Budget")
                print("0. Quit")
                choice = input("Enter your choice: ")
                if choice == "1":
                    bud = Budget.initialize("datagen_new.xlsx")
                    bud.display_info()
                    break
                elif choice == "2":
                    bud = Budget.initialize("datagen_new.xlsx")
                    bud.create_budget_process()
                    break
                elif choice == "3":
                    bud = Budget.initialize("datagen_new.xlsx")
                    bud.update_budget_process()
                    break
                elif choice == "0":
                    break
                else:
                    print("Invalid choice. Please select a valid option.")

        elif choice == "2":
            # Add Transaction
            print("What would you like to do?")
            while True:
                print("1. Manage Income")
                print("2. Manage expenses")
                print("0. Quit")
                choice = input("Enter your choice: ")
                if choice == "1":
                    Transaction.add_transaction("Income")
                    break
                elif choice == "2":
                    Transaction.add_transaction("Expenses")
                    break
                elif choice == "0":
                    break
                else:
                    print("Invalid choice. Please select a valid option.")

        elif choice == "3":
            print("What would you like to do?")
            while True:
                print("1. View Insights")
                print("2. Add Categories")
                print("0. Quit")
                choice = input("Enter your choice: ")
                if choice == "1":
                    # Example usage:
                    file_path = './datagen_new.xlsx'
                    analysis = ExpenseAnalysis(file_path)

                    # Display the first few rows of each DataFrame
                    analysis.display_data_head()

                    # Calculate and print budget vs actual values
                    analysis.calculate_budgeted_vs_actual()

                    # Process the expense data and calculate monthly, daily, and daily cumulative expenses
                    analysis.process_expense_data()
                    analysis.calculate_monthly_expenses()
                    analysis.calculate_daily_expenses()
                    analysis.calculate_daily_cumulative_sum()
                    analysis.calculate_daily_cumulative_sum_all_categories()  # New method to calculate total cumulative sum for all categories
                    analysis.calculate_daily_total_spending()  # New method to calculate total daily spending

                    # Plot the charts
                    analysis.plot_charts()
                    
                    break
                elif choice == "2":
                    cat = Category.initialize("./datagen_new.xlsx")
                    cat.create_category_process()
                    
                    break
                elif choice == "0":
                    break
                else:
                    print("Invalid choice. Please select a valid")

        elif choice == "0":
            print("Thank you for using the Expense Tracker.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

main()