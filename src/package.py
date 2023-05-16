import os
from urllib.parse import urljoin
from settings import DOWNLOADS, PACKAGE_EXTENSION, HASH_EXTENSION


class Package:
    def __init__(self, package_name, checksum_valid, base_url):
        self.package_name = package_name
        self.checksum_valid = checksum_valid
        self.base_url = base_url

        self.zip_file = PackageItem(urljoin(base_url, package_name + PACKAGE_EXTENSION),
                                    os.path.join(DOWNLOADS, self.package_name + PACKAGE_EXTENSION))
        self.hash_file = PackageItem(urljoin(base_url, package_name + HASH_EXTENSION),
                                     os.path.join(DOWNLOADS, self.package_name + HASH_EXTENSION))

    def __str__(self):
        return f'Package Name: {self.package_name}\nChecksum Valid: {self.checksum_valid}\nBase Url: {self.base_url}'


class PackageItem:
    def __init__(self, url, file_path):
        self.url = url
        self.file_path = file_path
