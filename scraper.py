import json
import requests
from bs4 import BeautifulSoup

# web scraper 2000 ultra larp edition

HEADERS = {
    "User-Agent": "cros-fetch/0.1"
}


def github_release(repo, release):
    url = f"https://api.github.com/repos/{repo}/releases/{release}"

    print(f"[GitHub] {repo}")

    r = requests.get(url, headers=HEADERS, timeout=20)
    r.raise_for_status()

    data = r.json()

    assets = []

    for asset in data.get("assets", []):
        assets.append({
            "name": asset["name"],
            "size": asset["size"],
            "download": asset["browser_download_url"]
        })

    return {
        "tag": data["tag_name"],
        "published": data["published_at"],
        "assets": assets
    }


def recovery_images():
    print("[MercuryWorkshop] Recovery Images")

    url = "https://cdn.jsdelivr.net/gh/MercuryWorkshop/chromeos-releases-data/data.json"

    r = requests.get(url, headers=HEADERS, timeout=30)
    r.raise_for_status()

    data = r.json()

    boards = {}

    for board, info in data.items():
        history = []

        for image in info.get("images", []):
            if image.get("last_modified", 0) == 0:
                continue

            history.append({
                "platform_version": image.get("platform_version"),
                "chrome_version": image.get("chrome_version"),
                "channel": image.get("channel"),
                "download": image.get("url"),
                "kernel_version": image.get("kernel_version"),
                "linux_version": image.get("linux_version"),
                "last_modified": image.get("last_modified"),
            })

        history.sort(key=lambda x: x["last_modified"], reverse=True)

        boards[board] = history

    print(f"Found {len(boards)} boards.")

    return boards


def rma_shims():
    print("[cros.download] RMA Shims")

    r = requests.get(
        "https://cros.download/shims",
        headers=HEADERS,
        timeout=20
    )
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")

    shims = []

    for a in soup.find_all("a", href=True):
        href = a["href"]

        if href.endswith(".zip"):
            shims.append({
                "board": a.text.replace(".zip", ""),
                "download": href
            })

    return shims


def main():
    db = {}

    try:
        db["legacy_sh1mmer"] = github_release(
            "crosbreaker/sh1mmer",
            "tags/legacy"
        )
    except Exception as e:
        print(e)

    try:
        db["badsh1mmer"] = github_release(
            "crosbreaker/badsh1mmer",
            "latest"
        )
    except Exception as e:
        print(e)

    try:
        db["recovery_images"] = recovery_images()
    except Exception as e:
        print(e)

    try:
        db["rma_shims"] = rma_shims()
    except Exception as e:
        print(e)

    with open("database.json", "w", encoding="utf-8") as f:
        json.dump(db, f, indent=4)

    print("\nSaved database.json")


def update_database():
    db = {}

    try:
        db["legacy_sh1mmer"] = github_release(
            "crosbreaker/sh1mmer",
            "tags/legacy"
        )
    except Exception as e:
        print(e)

    try:
        db["badsh1mmer"] = github_release(
            "crosbreaker/badsh1mmer",
            "latest"
        )
    except Exception as e:
        print(e)

    try:
        db["recovery_images"] = recovery_images()
    except Exception as e:
        print(e)

    try:
        db["rma_shims"] = rma_shims()
    except Exception as e:
        print(e)

    with open("database.json", "w", encoding="utf-8") as f:
        json.dump(db, f, indent=4)

    return db