from datetime import datetime

import os
import webuiapi
from PIL.PngImagePlugin import PngImageFile
from PIL import Image
from log import logger


sd_host = os.environ.get("SD_WEBUI_HOST", "127.0.0.1")
sd_port = os.environ.get("SD_WEBUI_PORT", "7860")
sd_webui_client = webuiapi.WebUIApi(host=sd_host, port=sd_port)


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
