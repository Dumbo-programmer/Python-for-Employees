#Slack Notifications
import requests

def send_slack_notification():
    print("Welcome to the Slack Notification Script!")
    message = input("Enter the message to send: ")
    webhook_url = input("Enter your Slack webhook URL: ")

    response = requests.post(webhook_url, json={"text": message})

    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Failed to send message.", response.json())

if __name__ == "__main__":
    send_slack_notification()
