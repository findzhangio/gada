import shutil
from fastapi import UploadFile


def save_image(file: UploadFile):
    try:
        file_name = "path_to_save_dir/" + file.filename
        with open(file_name, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return file_name
    finally:
        file.file.close()