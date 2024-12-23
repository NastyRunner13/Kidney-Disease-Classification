"""
This script sets up the initial directory structure and files for the Kidney Disease Classification project.
Imports:
    os: Provides a way of using operating system dependent functionality like reading or writing to the file system.
    pathlib.Path: Provides an object-oriented interface to the filesystem paths.
    logging: Provides a way to configure and use loggers in the code.
Logging Configuration:
    Configures the logging to display INFO level messages with a specific format.
Variables:
    project_name (str): The name of the project.
    list_of_files (list): A list of file paths to be created for the project.
Main Logic:
    Iterates over each file path in the list_of_files:
        - Splits the file path into directory and file name.
        - Creates the directory if it does not exist.
        - Creates the file if it does not exist or if it is empty.
        - Logs the creation of directories and files or if the file already exists.
"""

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = 'KidneyDiseaseClassifier'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath) or (os.path.getsize(filepath) == 0)):
        with open(filepath, 'w') as f:
            f.write('')
            logging.info(f"Creating File: {filepath}")
    
    else:
        logging.info(f"{filename} already exists in the directory")