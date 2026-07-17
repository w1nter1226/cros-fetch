# imports
import json
from scraper import update_database

# variables
version = 0.1
versiondate = "07/17/26"


while True:
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
        print("wip")
        print()

    elif choice == "2":
        print("wip")
        print()

    elif choice == "U":
        print("Starting Database update...")
        print()
        update_database()
        print()
        print("Database updated successfully!")
        print()
    
    elif choice == "C":
        print("tuff credits")
        print("created by me")
        print()

    elif choice == "E":
        print("Toodles :D")
        print()
        break

    else:
        print(f"'{choice}' is not a valid option!")