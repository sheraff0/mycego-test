from .disk import YaDiskFolder
from .images import extract_image, write_images


def load_and_convert(link):
    folder = YaDiskFolder(link)
    folder.download()
    files_list = folder.files_list()

    _images = []

    for file in files_list:
        _img = extract_image(folder.zip_file, file)
        if _img is not None:
            _images.append(_img)

    if _images:
        return write_images(_images)
