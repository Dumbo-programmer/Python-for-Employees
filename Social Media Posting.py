import requests

def post_to_social_media():
    print("Welcome to the Social Media Posting Script!")
    platform = input("Enter the platform (Twitter/Facebook): ").lower()
    message = input("Enter the message to post: ")
    api_key = input(f"Enter your {platform.capitalize()} API key: ")

    if platform == "twitter":
        url = "https://api.twitter.com/2/tweets"
        headers = {"Authorization": f"Bearer {api_key}"}
        data = {"text": message}
    elif platform == "facebook":
        url = f"https://graph.facebook.com/me/feed?message={message}&access_token={api_key}"
        headers = {}
        data = {}
    else:
        print("Unsupported platform.")
        return

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Message posted successfully!")
    else:
        print("Failed to post message.", response.json())

if __name__ == "__main__":
    post_to_social_media()
