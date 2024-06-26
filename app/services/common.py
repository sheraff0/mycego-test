import numpy as np

from .disk import YaDiskFolder
from .images import extract_image, write_images


def load_and_convert(link):
    folder = YaDiskFolder(link)
    folder.download()
    files_list = folder.files_list()

    images = [_img for file in files_list
        if (_img := extract_image(folder.zip_file, file))]

    if images:
        return write_images(images)
