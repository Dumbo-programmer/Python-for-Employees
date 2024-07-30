import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    print("Welcome to the Email Automation Script!")
    sender_email = input("Enter your email: ")
    receiver_email = input("Enter the receiver's email: ")
    subject = input("Enter the email subject: ")
    body = input("Enter the email body: ")

    # Email configuration
    smtp_server = "smtp.example.com"
    smtp_port = 587
    password = input("Enter your email password: ")

    # Create the email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(message)
        print("Email sent successfully!")

if __name__ == "__main__":
    send_email()
