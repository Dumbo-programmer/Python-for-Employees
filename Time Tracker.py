#Time Tracker
import time

def time_tracker():
    print("Welcome to the Time Tracker Script!")
    task = input("Enter the task you are working on: ")
    start_time = time.time()

    input("Press Enter to stop tracking time...")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time spent on {task}: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    time_tracker()
