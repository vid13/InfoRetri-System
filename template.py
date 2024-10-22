import os
from pathlib import Path

import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
]

for fpath in list_of_files:
    fpath = Path(fpath)
    fdir, fname = os.path.split(fpath)

    if fdir !="":
        os.makedirs(fdir, exist_ok=True)
        logging.info(f"Creating dir {fdir} for the file {fname}")
    
    if (not os.path.exists(fpath)) or (os.path.getize(fpath)==0):
        with open(fpath, "w") as f:
            pass
        logging.info(f"creating empty file: {fpath}")
    else:
        logging.info(f"{fname} already exists")