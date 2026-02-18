import time
from datetime import datetime
import os

LOG_FILE = "study_log.txt"


def start_study():
    subject = input("Enter subject name: ")
    print("Study session started... Press ENTER to stop.")
    
    start_time = time.time()
    input()  # Wait for user to press Enter
    end_time = time.time()

    duration = end_time - start_time
    minutes = round(duration / 60, 2)

    save_session(subject, minutes)
    print(f"Study session saved! Duration: {minutes} minutes.")


def save_session(subject, minutes):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as file:
        file.write(f"{date} | {subject} | {minutes} minutes\n")


def view_total_time():
    if not os.path.exists(LOG_FILE):
        print("No study records found.")
        return

    total_minutes = 0

    with open(LOG_FILE, "r") as file:
        for line in file:
            parts = line.strip().split("|")
            minutes = float(parts[2].replace("minutes", "").strip())
            total_minutes += minutes

    print(f"Total Study Time: {round(total_minutes, 2)} minutes")


def view_log():
    if not os.path.exists(LOG_FILE):
        print("No study records found.")
        return

    print("\n--- Study Log ---")
    with open(LOG_FILE, "r") as file:
        print(file.read())


def main():
    while True:
        print("\n=== Student Study Time Tracker ===")
        print("1. Start Study Session")
        print("2. View Total Study Time")
        print("3. View Study Log")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            start_study()
        elif choice == "2":
            view_total_time()
        elif choice == "3":
            view_log()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
