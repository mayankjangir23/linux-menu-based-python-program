import os
import time
import getpass

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def login():
    clear()
    print("=== Linux Automation Login ===")
    username = input("Enter Linux username: ")
    ip = input("Enter IP address (leave blank for local): ")
    password = getpass.getpass("Enter password: ")
    print("\nLogging in as", username, "...")
    time.sleep(1)
    print("Login successful!\n")
    time.sleep(1)
    return username, ip

def menu():
    print("\n=== Linux Command Automation Menu ===")
    print("1. Show current directory")
    print("2. List files in directory")
    print("3. Show disk usage")
    print("4. Show active processes")
    print("5. Show current user")
    print("6. Show system uptime")
    print("7. Create a new directory")
    print("8. Remove a file")
    print("9. Show IP address")
    print("10. Check system memory")
    print("0. Exit")
    print("====================================")

def run_command(choice):
    if choice == '1':
        os.system("pwd")
    elif choice == '2':
        os.system("ls -l")
    elif choice == '3':
        os.system("df -h")
    elif choice == '4':
        os.system("ps aux")
    elif choice == '5':
        os.system("whoami")
    elif choice == '6':
        os.system("uptime")
    elif choice == '7':
        dirname = input("Enter directory name to create: ")
        os.system(f"mkdir -p {dirname}")
    elif choice == '8':
        filename = input("Enter filename to remove: ")
        os.system(f"rm -i {filename}")
    elif choice == '9':
        os.system("ip a")
    elif choice == '10':
        os.system("free -h")
    elif choice == '0':
        print("Exiting...")
        time.sleep(1)
        return False
    else:
        print("Invalid choice.")
    return True

def main():
    username, ip = login()
    while True:
        clear()
        print(f"Connected as {username} @ {ip if ip else 'localhost'}")
        menu()
        choice = input("Enter your choice: ")
        if not run_command(choice):
            break
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
