from io import BytesIO

import cv2

import imageio.v3 as iio


def extract_image(zip_file, filename):
    try:
        with zip_file.open(filename) as f:
            return cv2.imread(f)
    except:
        ...


def write_images(images):
    output = BytesIO()
    iio.imwrite(output, images, extension=".tif")
    output.seek(0)
    return output
