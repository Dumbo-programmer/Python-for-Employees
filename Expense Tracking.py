import pandas as pd

def track_expenses():
    print("Welcome to the Expense Tracking Script!")
    expenses = []
    num_expenses = int(input("How many expenses do you want to enter? "))
    
    for _ in range(num_expenses):
        description = input("Enter expense description: ")
        amount = float(input("Enter expense amount: "))
        date = input("Enter expense date (YYYY-MM-DD): ")
        expenses.append({"Description": description, "Amount": amount, "Date": date})
    
    df = pd.DataFrame(expenses)
    df.to_csv("expenses.csv", index=False)
    print("Expenses saved to expenses.csv")

if __name__ == "__main__":
    track_expenses()
