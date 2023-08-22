from datetime import datetime
from PIL.PngImagePlugin import PngImageFile
from log import logger
from os import path, mkdir, environ


def save_img(img, filename=None):
    image_cache_path = environ.get('IMAGE_CACHE_PATH', './tmp/')
    if filename is None:
        filename = str(datetime.timestamp(datetime.now())) + ".png"

    elif len(filename.strip()) == 0:
        filename = str(datetime.timestamp(datetime.now())) + ".png"
    else:
        filename = filename

    if not path.exists(image_cache_path):
        mkdir(image_cache_path)
    image_path_file = image_cache_path + filename
    PngImageFile.save(img, image_path_file)
    logger.debug("filename: %s", filename)
    return filename
