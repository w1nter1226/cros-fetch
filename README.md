# cros-fetch
A tool to make writing recovery USBs and RMA shims for Chromebooks easier than ever

## How to use

> When you first use cros-fetch, update the database first before downloading any shims/reco images!
> (Press U on the main menu to update the database)

Windows:
```powershell
git clone https://github.com/w1nter1226/cros-fetch.git
cd cros-fetch
pip install -r requirements.txt
python main.py
```


macOS/Linux:
```bash
git clone https://github.com/w1nter1226/cros-fetch.git
cd cros-fetch
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

### Disclaimer

- cros-fetch is an independent project and is not affiliated with Google LLC. 

- While cros-fetch provides utilities known for enrollment escapes, This tool is intended **only** for legitimate hardware recovery and authorized RMA tasks.