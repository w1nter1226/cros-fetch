import os

from download import download_file


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress Enter to continue...")


def menu(title, options):
    """
    Menu with:
    - Number selection
    - Name selection
    - Back option
    """

    while True:
        clear()

        print()

        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        print()
        print(title)
        print("(Type a number or name, B to go back)")
        
        choice = input("> ").strip()

        if choice.upper() == "B":
            return None

        # Number selection
        if choice.isdigit():

            index = int(choice) - 1

            if 0 <= index < len(options):
                return index

        # Name selection
        for index, option in enumerate(options):

            if choice.lower() == option.lower():
                return index

        print("\nInvalid option!")
        input("Press Enter to retry...")


############################################################
# RECOVERY IMAGES
############################################################

def recovery_menu(db):

    boards = sorted(db["recovery_images"].keys())

    board_index = menu(
        "Choose the target Chromebook's baseboard",
        boards
    )

    if board_index is None:
        return

    board = boards[board_index]

    image_type = menu(
        f"Choose image type for {board}",
        [
            "Normal Recovery Image",
            "Badsh1mmer"
        ]
    )

    if image_type is None:
        return

    if image_type == 0:
        recovery_versions(db, board)

    else:
        badsh1mmer_download(db, board)


def recovery_versions(db, board):

    images = db["recovery_images"][board]

    options = []

    for image in images:

        channel = image["channel"].replace("-channel", "").title()

        options.append(
            f"ChromeOS {image['chrome_version']} "
            f"{channel} "
            f"KV{image['kernel_version']}"
        )

    version = menu(
        f"Choose Recovery Version for {board}",
        options
    )

    if version is None:
        return

    image = images[version]

    filename = os.path.basename(image["download"])

    download_file(
        image["download"],
        filename
    )

    pause()


def badsh1mmer_download(db, board):

    for asset in db["badsh1mmer"]["assets"]:

        if asset["name"] == f"badsh1mmer-{board}.zip":

            download_file(
                asset["download"],
                asset["name"]
            )

            pause()
            return

    print("\nNo Badsh1mmer build exists for this board :[")
    pause()


############################################################
# SHIMS
############################################################

def shim_menu(db):

    boards = sorted(
        shim["board"]
        for shim in db["rma_shims"]
    )

    board_index = menu(
        "Choose the target Chromebook's baseboard",
        boards
    )

    if board_index is None:
        return

    board = boards[board_index]

    shim_type = menu(
        f"Do you want a modded shim for {board}?",
        [
            "Normal RMA Shim",
            "Modded Shim"
        ]
    )

    if shim_type is None:
        return

    if shim_type == 0:
        download_rma_shim(db, board)

    else:
        modded_shim_menu(db, board)


############################################################
# NORMAL SHIMS
############################################################

def download_rma_shim(db, board):

    for shim in db["rma_shims"]:

        if shim["board"] == board:

            download_file(
                shim["download"],
                f"{board}.zip"
            )

            pause()
            return

    print("\nNo RMA shim exists.")
    pause()


############################################################
# MODDED SHIMS
############################################################

def modded_shim_menu(db, board):

    choice = menu(
        f"Choose Modded Shim for {board}",
        [
            "Legacy SH1mmer",
            "Cr3nroll Shim"
        ]
    )

    if choice is None:
        return

    if choice == 0:
        release = db["legacy_sh1mmer"]

    else:
        release = db["cr3nroll-shim"]

    for asset in release["assets"]:

        if asset["name"].startswith(board):

            download_file(
                asset["download"],
                asset["name"]
            )

            pause()
            return

    print("\nNo build exists for this board.")
    pause()