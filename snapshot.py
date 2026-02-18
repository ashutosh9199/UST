import subprocess
import os
import difflib
from datetime import datetime
print ("hello world")


def get_installed_packages():
    try:
        result = subprocess.check_output(["pip", "freeze"], text=True)
        return result
    except:
        return "Could not retrieve installed packages\n"


def get_environment_variables():
    env_vars = ""
    for key, value in os.environ.items():
        env_vars += f"{key}={value}\n"
    return env_vars


def get_active_users():
    try:
        # Windows
        result = subprocess.check_output(["query", "user"], text=True)
    except:
        try:
            # Linux / Mac
            result = subprocess.check_output(["who"], text=True)
        except:
            result = "Could not retrieve active users\n"

    return result


def create_snapshot():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"snapshot_{timestamp}.txt"

    with open(filename, "w") as f:
        f.write("=== INSTALLED PACKAGES ===\n")
        f.write(get_installed_packages())
        f.write("\n=== ENVIRONMENT VARIABLES ===\n")
        f.write(get_environment_variables())
        f.write("\n=== ACTIVE USERS ===\n")
        f.write(get_active_users())

    print(f"[+] Snapshot saved as {filename}")
    return filename


def compare_snapshots(file1, file2):
    with open(file1, "r") as f1, open(file2, "r") as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    diff = difflib.unified_diff(
        lines1,
        lines2,
        fromfile=file1,
        tofile=file2,
        lineterm=""
    )

    print("\n".join(diff))


def main():
    print("=== System Snapshot Tool ===")
    print("1. Create Snapshot")
    print("2. Compare Snapshots")

    choice = input("Select option: ")

    if choice == "1":
        create_snapshot()

    elif choice == "2":
        file1 = input("Enter first snapshot filename: ")
        file2 = input("Enter second snapshot filename: ")
        compare_snapshots(file1, file2)

    else:
        print("Invalid option")


if __name__ == "__main__":
    main()
