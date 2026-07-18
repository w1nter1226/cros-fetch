import os
import zipfile
import requests

from rich.progress import (
    Progress,
    BarColumn,
    DownloadColumn,
    TransferSpeedColumn,
    TimeRemainingColumn,
)

def download_file(url, filename):
    os.makedirs("downloads", exist_ok=True)
    filepath = os.path.join("downloads", filename)

    response = requests.get(url, stream=True)
    response.raise_for_status()
    total = int(response.headers.get("content-length", 0))

    with Progress(          
        "[bold white]{task.description}",               
        BarColumn(bar_width=30, complete_style="white", finished_style="green"),
        "[progress.percentage]{task.percentage:>3.0f}%",
        "•",
        DownloadColumn(),                             
        "•",
        TransferSpeedColumn(),                         
        "•",
        TimeRemainingColumn(),                         
    ) as progress:

        task = progress.add_task(f"Downloading {filename}", total=total)

        with open(filepath, "wb") as f:
            for chunk in response.iter_content(8192):
                if chunk:
                    f.write(chunk)
                    progress.update(task, advance=len(chunk))

    print(f"\nDownload complete! Saved to {filepath}")

    if filename.endswith(".zip"):
        extract_to = "downloads/extracted"
        print(f"Extracting {filename}...")
        os.makedirs(extract_to, exist_ok=True)
        
        with zipfile.ZipFile(filepath, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
            
        print(f"Extraction complete! Saved to {extract_to}")