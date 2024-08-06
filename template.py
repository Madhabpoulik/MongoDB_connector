import os
from pathlib import Path
import logging

package_name = "mongodb_connector"

list_of_files =[
    ".github/workflows/ci.yaml",
    f"src/__init__.py",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/mongo_crud.py",
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/unit/ut_mongo_crud.py",
    f"tests/integration/__init__.py",
    f"tests/integration/it_mongo_crud.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    f"research/trials.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir, filename = os.path.split(filepath)
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_dir} for file: {filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")
