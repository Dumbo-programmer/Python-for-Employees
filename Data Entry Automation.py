import pandas as pd

def data_entry():
    print("Welcome to the Data Entry Automation Script!")
    data = []
    num_entries = int(input("How many entries do you want to add? "))
    
    for _ in range(num_entries):
        name = input("Enter name: ")
        age = input("Enter age: ")
        email = input("Enter email: ")
        data.append({"Name": name, "Age": age, "Email": email})
    
    df = pd.DataFrame(data)
    df.to_csv("employee_data.csv", index=False)
    print("Data saved to employee_data.csv")

if __name__ == "__main__":
    data_entry()
