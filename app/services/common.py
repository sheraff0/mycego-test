import numpy as np

from fastapi import HTTPException

from .disk import YaDiskFolder
from .images import extract_image, write_images


def load_and_convert(link):
    try:
        folder = YaDiskFolder(link)
        folder.download()
        files_list = folder.files_list()
    except:
        raise HTTPException(400, "Cannot read files!")

    images = []

    for file in files_list:
        img = extract_image(folder.zip_file, file)
        if img is not None:
            images.append(img)

    return write_images(images)
