from datetime import datetime

import webuiapi
from PIL.PngImagePlugin import PngImageFile
from PIL import Image
from log import logger
from config import Config


sd_webui_client = webuiapi.WebUIApi(host=Config.SD_WEBUI_HOST, port=Config.SD_WEBUI_PORT)


def save_img(img, filename=None):
    if filename is None:
        filename = "/tmp/" + str(datetime.timestamp(datetime.now())) + ".png"

    elif len(filename.strip()) == 0:
        filename = "/tmp/" + str(datetime.timestamp(datetime.now())) + ".png"
    else:
        filename = "/tmp/" + filename
    PngImageFile.save(img, filename)
    logger.debug("filename: %s", filename)
    return filename


def openpose(filename):
    img = Image.open(filename)
    unit = webuiapi.ControlNetUnit(input_image=img, module='openpose_full', model='control_v11p_sd15_openpose_fp16 ['
                                                                                  '73c2b67d]')
    return unit
