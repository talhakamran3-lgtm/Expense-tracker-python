from turtle import pd

import matplotlib.pyplot as plt
from expense import Expense
import expense
import calendar
import datetime
3

import numpy as np
from datetime import date, datetime

def show_menu():
    print("Please select an option:")
    print("1. Add a new expense")
    print("2. View total expenses and remaining budget")
    print("3. Visualize expenses by category")
    print("4. Exit")

def main():
    print(f"Welcome to the Expense Tracker! 🎉")
    expense_file_path = "expense.csv"
    
    #writing sub function to:

    while True:
        show_menu()
        choice = input("Enter your choice (1-3):")
        if choice == "1":
            #get user input for expense details

            expense = get_user_expense()
            save_expense_to_file(expense, expense_file_path)

        elif choice == "2":
            Budget = 10000.00  # Example budget, you can modify this as needed
            summarize_expense(expense_file_path, Budget)


        elif choice == "4":
            print("Thank you for using the Expense Tracker! Goodbye! 👋")
            break

        elif choice == "3":
            visualize_by_category(expense_file_path)
            print("Thank you for using the Expense Tracker! Goodbye! 👋")
            break


        else:
            print("Invalid choice. Please try again.")

    
    
    





#defining sub function to get user input for expense details
def get_user_expense():
    print("Please enter the details of your expense:")
    expense_name = input("Enter Expense name:")
    expense_amount = float(input("Enter Expense amount:"))  
    print(f"You have entered: {expense_name} with amount {expense_amount}")
    #for category
    expense_category = [
    "FOOD 🍔",
    "TRANSPORTATION 🚗",
    "STUDY 📚",
    "HOUSING 🏠",
    "UTILITIES 💡",
    "FUN 🎉"
    ]


    while True:
        print("Please select a category for your expense:")
        for i, category in enumerate(expense_category):
            print(f"{i+1}. {category}")
        category_choice = input("Enter the number corresponding to the category:")
        if category_choice.isdigit() and 1 <= int(category_choice) <= len(expense_category):
            selected_category = expense_category[int(category_choice) - 1]
            current_datetime = datetime.now().strftime
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount, date=current_datetime)
            return new_expense
        else:
            print("Invalid choice. Please try again.")

# defining sub function to save the expense details in a file
def save_expense_to_file(expense, expense_file_path):
    print(f"Saving expense: {expense} to file: {expense_file_path}")
    
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    with open(expense_file_path, "a", encoding="utf-8") as file:
        file.write(
            f"{expense.name},{expense.category},{expense.amount},{formatted_datetime}\n"
        )

#defining sub function to summarize the expenses by category
def summarize_expense(expense_file_path, Budget):
    print(f"Summarizing expenses from file: {expense_file_path}")
    expense:list[Expense] = []
    with open(expense_file_path, "r", encoding="utf-8") as file:
        lines= file.readlines()
        for line in lines:
            expense_name, expense_category, expense_amount, expense_datetime = line.strip().split(",")
            #creating an expense object and adding it to the list
            line_expense =Expense(
                name=expense_name, amount=float(expense_amount),category=expense_category, date = expense_datetime)
                                  
            expense.append(line_expense)
#summarizing the expenses by category
            amount_by_category = {}

            for exp in expense:
                key = exp.category
                if key in amount_by_category:
                        amount_by_category[key] += exp.amount
                else:
                    amount_by_category[key] = exp.amount



    #displaying the summarized expenses by category
    for key, amount in amount_by_category.items():
        print(f"Category: {key}, Total Amount: ${amount:,.2f}")

    #displaying the total expenses and remaining budget
    total_spent = sum([exp.amount for exp in expense])
    remaining_budget = Budget - total_spent
    print(f"💰 Total Expenses: ${total_spent:,.2f}")
    print(f"💰 Remaining Budget: ${remaining_budget:,.2f}")

    #displaying budget per day 
    today = date.today()
    days_in_month = calendar.monthrange(today.year, today.month)[1]
    remaining_days = days_in_month - today.day
    daily_budget = remaining_budget / remaining_days if remaining_days > 0 else 0

    print(green_text(f"📅 Daily Budget for the rest of the month: ${daily_budget:,.2f}"))

    #displaying the highest spending category
    highest_spending_category = max(amount_by_category, key=amount_by_category.get)
    highest_amount = amount_by_category[highest_spending_category]
    print(green_text(f"📊 Highest Spending Category: {highest_spending_category} with amount ${highest_amount:,.2f}"))
#to stand out the outputs 
def green_text(text):
    return f"\033[92m{text}\033[0m"

import matplotlib.pyplot as plt

def visualize_by_category(expense_file_path):
    expense_list = []

    # Read file and create Expense objects
    with open(expense_file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

        for line in lines:
            expense_name, expense_category, expense_amount, expense_datetime = (
                line.strip().split(",")
            )

            exp = Expense(
                name=expense_name,
                category=expense_category,
                amount=float(expense_amount),
                date=expense_datetime,
            )

            expense_list.append(exp)

    # Calculate total amount by category
    amount_by_category = {}

    for exp in expense_list:
        key = exp.category
        if key in amount_by_category:
            amount_by_category[key] += exp.amount
        else:
            amount_by_category[key] = exp.amount

    # --- PLOT PIE CHART ---
    plt.figure()
    plt.pie(
        amount_by_category.values(),
        labels=amount_by_category.keys(),
        autopct="%1.1f%%"
    )
    plt.title("Spending by Category")
    plt.show()



#Main function to run the program
if __name__ == "__main__":
    main()