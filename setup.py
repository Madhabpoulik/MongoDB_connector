from setuptools import find_packages,setup
from typing import List
import os

HYPEN_E_DOT = "-e ."

def get_requirement(file_path:str)->List[str]:
    print(f"Reading {file_path}")
    requirements = []
    file_path = os.path.join(os.path.dirname(__file__),file_path)
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "1.0.0"
REPO_NAME = "MongoDB_connector"
PKG_NAME = "MongoConn"
AUTHOR_USER_NAME = "Madhabpoulik"  
AUTHOR_EMAIL = "madhabpoulik97@gmail.com"

setup(
    name=PKG_NAME,
    version = __version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for mongodb connector",
    long_description=long_description,
    long_description_content = "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=find_packages(where="src"),
    install_requires= ["pymongo>=4.0"]
)
# MongoDB_connector/requirements_dev.txt