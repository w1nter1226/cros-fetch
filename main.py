# imports
import json
import subprocess
import os
from scraper import update_database

# variables
version = 0.2
versiondate = "07/17/26"
database = "database.json"

def clear_screen():
    # 'nt' means Windows, 'posix' is Mac/Linux
    subprocess.run('cls' if os.name == 'nt' else 'clear')

while True:
    clear_screen()

    # ooohhhh ascii title so tuff
    print("""
 ██████╗██████╗  ██████╗ ███████╗      ███████╗███████╗████████╗ ██████╗██╗  ██╗
██╔════╝██╔══██╗██╔═══██╗██╔════╝      ██╔════╝██╔════╝╚══██╔══╝██╔════╝██║  ██║
██║     ██████╔╝██║   ██║███████╗█████╗█████╗  █████╗     ██║   ██║     ███████║
██║     ██╔══██╗██║   ██║╚════██║╚════╝██╔══╝  ██╔══╝     ██║   ██║     ██╔══██║
╚██████╗██║  ██║╚██████╔╝███████║      ██║     ███████╗   ██║   ╚██████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝      ╚═╝     ╚══════╝   ╚═╝    ╚═════╝╚═╝  ╚═╝
""")
    print(f"v{version} | {versiondate}")
    print("Developed by w1nter1226 on GitHub")
    print("https://github.com/w1nter1226/cros-fetch")
    if not os.path.exists(database):
        print()
        print("database.json not found! :[")
        print("Please update the database before downloading shims/reco images")
    print()


    # custom tui because i dont wanna learn textual
    print("--- Main Menu ---")
    print("1. Recovery Images")
    print("2. Shims")
    print("U. Update Database")
    print("C. Credits")
    print("E. Exit")
    print()

    choice = input("> ").strip().upper()
    print()

    if choice == "1":
        print("wip!! sorry :(")
        print()
        input("\nPress Enter to continue")

    elif choice == "2":
        print("wip!! sorry :(")
        print()
        input("\nPress Enter to continue")

    elif choice == "U":
        print("Starting Database update...")
        print()
        update_database()
        print()
        print("Database updated successfully!")
        print()
        input("\nPress Enter to continue")
    
    elif choice == "C":
        print("tuff credits")
        print("created by me")
        print()
        input("\nPress Enter to continue")

    elif choice == "E":
        print("Toodles :D")
        print()
        break

    else:
        print(f"'{choice}' is not a valid option!")