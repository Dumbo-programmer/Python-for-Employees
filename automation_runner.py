import os
import subprocess

# List of available automation scripts
scripts = [
    "Email Automation",
    "Data Entry Automation",
    "File Management",
    "Report Generation",
    "Meeting Scheduler",
    "Web Scraping",
    "Employee Onboarding",
    "Expense Tracking",
    "Performance Metrics",
    "Task Management",
    "Social Media Posting",
    "Backup Files",
    "Text Translation",
    "Weather Forecast",
    "Convert Currency",
    "PDF Merger",
    "Slack Notifications",
    "Website Status Checker",
    "Generate QR Code",
    "Time Tracker"
]

def list_scripts():
    print("Available Automation Scripts:")
    for index, script in enumerate(scripts, start=1):
        print(f"{index}. {script}")

def run_script(script_name):
    try:
        # Running the script by calling a Python file named after the script (e.g., email_automation.py)
        script_filename = script_name.lower().replace(' ', '_') + ".py"
        subprocess.run(["python", script_filename], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running script {script_name}: {e}")
    except FileNotFoundError:
        print(f"Script file '{script_filename}' not found. Please make sure it exists.")

def main():
    while True:
        list_scripts()
        choice = input("\nEnter the number of the script to run (or 'q' to quit): ")
        
        if choice.lower() == 'q':
            print("Exiting the automation runner. Goodbye!")
            break
        
        if choice.isdigit() and 1 <= int(choice) <= len(scripts):
            script_index = int(choice) - 1
            script_to_run = scripts[script_index]
            print(f"\nRunning script: {script_to_run}")
            run_script(script_to_run)
        else:
            print("Invalid choice. Please enter a number corresponding to a script or 'q' to quit.")

if __name__ == "__main__":
    main()
