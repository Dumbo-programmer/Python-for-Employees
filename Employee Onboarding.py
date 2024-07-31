#EMPLOYEE ONBOARDING
import os

def onboarding():
    print("Welcome to the Employee Onboarding Script!")
    username = input("Enter the new employee's username: ")
    email = input("Enter the new employee's email: ")

    # Create a new folder for the employee
    os.makedirs(f"onboarding/{username}", exist_ok=True)
    
    with open(f"onboarding/{username}/welcome.txt", "w") as f:
        f.write(f"Welcome {username}!\n")
        f.write(f"Your email is {email}\n")
        f.write("Please follow the instructions to complete your onboarding process.")

    print(f"Onboarding folder created for {username}")

if __name__ == "__main__":
    onboarding()
