import os
import yaml
import json
import joblib
import base64
from typing import Any
from pathlib import Path
from box import ConfigBox
from ensure import ensure_annotations
from box.exceptions import BoxValueError
from KidneyDiseaseClassifier import logger

@ensure_annotations
def read_yaml(path_to_yaml : Path) -> ConfigBox:
    """
    Read the yaml file and return the ConfigBox object.
    """
    try:
        with open(path_to_yaml, "r") as file:
            content = yaml.safe_load(file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty.")
    except Exception as e:
        raise e
    
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create directories if they do not exist.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created: {path}")


@ensure_annotations
def save_json(path: Path, date: dict):
    """
    Save the dictionary as a json file.
    """
    with open(path, "w") as file:
        json.dump(date, file, indent=4)
    logger.info(f"json file: {path} saved successfully.")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load the json file and return the ConfigBox object.
    """
    with open(path, "r") as file:
        content = json.load(file)
    logger.info(f"json file: {path} loaded successfully.")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save the data as a binary file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary File: {path} saved successfully.")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load the binary file and return the data.
    """
    data = joblib.load(filename=path)
    logger.info(f"Binary File: {path} loaded successfully.")
    return data


@ensure_annotations
def get_size(path: Path) -> int:
    """
    Return the size of the file in bytes.
    """
    return os.path.getsize(path) + " MB"


def decodeImage(imgString, filename):
    img_data = base64.b64decode(imgString)
    with open(filename, 'wb') as file:
        file.write(img_data)
        file.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')  