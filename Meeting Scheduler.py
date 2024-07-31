from datetime import datetime
import calendar

def schedule_meeting():
    print("Welcome to the Meeting Scheduler Script!")
    meeting_date = input("Enter the meeting date (YYYY-MM-DD): ")
    meeting_time = input("Enter the meeting time (HH:MM): ")
    meeting_subject = input("Enter the meeting subject: ")
    
    try:
        date_time = datetime.strptime(f"{meeting_date} {meeting_time}", "%Y-%m-%d %H:%M")
        print(f"Meeting scheduled for {date_time} with subject '{meeting_subject}'.")
    except ValueError:
        print("Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time.")

if __name__ == "__main__":
    schedule_meeting()
