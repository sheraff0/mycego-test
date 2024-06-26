from io import BytesIO

import cv2
import imageio.v3 as iio
import numpy as np


def extract_image(zip_file, filename):
    try:
        with zip_file.open(filename) as f:
            img = cv2.imdecode(np.frombuffer(f.read(), np.uint8), 1)
            return img
    except:
        ...


def write_images(images):
    output = BytesIO()
    iio.imwrite(output, images, plugin="tifffile", extension=".tif")
    output.seek(0)
    return output
