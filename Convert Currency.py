#Convert Currency
import requests

def convert_currency():
    print("Welcome to the Currency Conversion Script!")
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the source currency code (e.g., 'USD'): ").upper()
    to_currency = input("Enter the target currency code (e.g., 'EUR'): ").upper()
    api_key = input("Enter your currency conversion API key: ")

    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        rate = data['rates'][to_currency]
        converted_amount = amount * rate
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    else:
        print("Failed to retrieve currency data.", data)

if __name__ == "__main__":
    convert_currency()
