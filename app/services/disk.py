from io import BytesIO
from typing import List
from zipfile import ZipFile

from yadisk import Client


class YaDiskFolder:
    def __init__(self, public_url: str):
        self.public_url = public_url
        self.client = Client()

    def download(self) -> None:
        _buffer = BytesIO()
        self.client.download_public(self.public_url, _buffer)
        self.zip_file = ZipFile(_buffer)

    def list(self) -> List[str]:
        return self.zip_file.namelist()

    def files_list(self) -> List[str]:
        return [x for x in self.list() if not x.endswith("/")]
