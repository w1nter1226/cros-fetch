import json
import os
import subprocess
import shutil

from scraper import update_database
from menus import recovery_menu, shim_menu

VERSION = "0.5"
VERSION_DATE = "07/17/26"
DATABASE = "database.json"


def clear_screen():
    subprocess.run(
        "cls" if os.name == "nt" else "clear",
        shell=True
    )


def load_database():
    if not os.path.exists(DATABASE):
        return None

    with open(DATABASE, "r", encoding="utf-8") as f:
        return json.load(f)
    
def delete_downloads():
    folder = "downloads"
    
    if os.path.exists(folder):
        shutil.rmtree(folder)
    else:
        print("Downloads folder not found?")


def header():
    clear_screen()

    print(r"""
 ██████╗██████╗  ██████╗ ███████╗      ███████╗███████╗████████╗ ██████╗██╗  ██╗
██╔════╝██╔══██╗██╔═══██╗██╔════╝      ██╔════╝██╔════╝╚══██╔══╝██╔════╝██║  ██║
██║     ██████╔╝██║   ██║███████╗█████╗█████╗  █████╗     ██║   ██║     ███████║
██║     ██╔══██╗██║   ██║╚════██║╚════╝██╔══╝  ██╔══╝     ██║   ██║     ██╔══██║
╚██████╗██║  ██║╚██████╔╝███████║      ██║     ███████╗   ██║   ╚██████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝      ╚═╝     ╚══════╝   ╚═╝    ╚═════╝╚═╝  ╚═╝
""")

    print(f"v{VERSION} | {VERSION_DATE}")
    print("Developed by w1nter1226 on GitHub")
    print("https://github.com/w1nter1226/cros-fetch")
    print()

    if not os.path.exists(DATABASE):
        print("database.json not found!")
        print("Please update the database before downloading.")
        print()


def pause():
    input("\nPress Enter to continue...")


while True:
    header()

    print("--- Main Menu ---")
    print("1. Recovery Images")
    print("2. Shims")
    print("U. Update Database")
    print("D. Delete Downloads")
    print("C. Credits")
    print("E. Exit")
    print()

    choice = input("> ").strip().upper()

    if choice == "1":

        db = load_database()

        if db is None:
            print("\nDatabase not found.")
            pause()
            continue

        recovery_menu(db)

    elif choice == "2":

        db = load_database()

        if db is None:
            print("\nDatabase not found.")
            pause()
            continue

        shim_menu(db)

    elif choice == "U":

        print("\nUpdating database...\n")
        update_database()

        print("\nDatabase updated successfully!")
        pause()

    elif choice == "D":

        print("\nDeleting downloaded reco images and shims...")
        delete_downloads()
        pause()

    elif choice == "C":

        print("\nCredits")
        print("-------")
        print("Developed by w1nter1226")
        print("Recovery images from Google")
        print("RMA shims from dl.cros.download")
        print("SH1mmer & Badsh1mmer from Crosbreaker")
        print("Cr3nroll from CrOSmium")

        pause()

    elif choice == "E":

        print("\nGoodbye!")
        break

    else:

        print(f"\n'{choice}' is not a valid option.")
        pause()