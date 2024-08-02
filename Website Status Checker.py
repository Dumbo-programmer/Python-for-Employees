#Website Status Checker
import requests

def check_website_status():
    print("Welcome to the Website Status Checker Script!")
    url = input("Enter the website URL: ")

    response = requests.get(url)
    if response.status_code == 200:
        print(f"The website {url} is up and running.")
    else:
        print(f"The website {url} is down. Status code: {response.status_code}")

if __name__ == "__main__":
    check_website_status()
