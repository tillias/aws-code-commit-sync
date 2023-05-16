import hashlib
import shutil
import os
import urllib.request

from package import Package
from settings import EXTRACT_PATH


class PackageDownloader:
    def download_and_validate_package(self, url, package_name):

        package = Package(package_name, False, url)
        zip_url = package.zip_file.url
        zip_path = package.zip_file.file_path

        print(f"Downloading package {zip_url} into: {zip_path}")
        urllib.request.urlretrieve(zip_url, zip_path)

        hash_url = package.hash_file.url
        hash_path = package.hash_file.file_path

        print(f"Downloading hash {hash_url} into: {hash_path}")
        urllib.request.urlretrieve(hash_url, hash_path)

        package.checksum_valid = self.__validate_package(package)

        return package

    def cleanup(self, package):
        extract_path = os.path.join(EXTRACT_PATH, package.package_name)
        print(f'Removing extracted package contents from {extract_path}')
        shutil.rmtree(extract_path)

        print(f'Removing package hash and zip files...')
        os.remove(package.zip_file.file_path)
        os.remove(package.hash_file.file_path)

    def __validate_package(self, package):
        stored_hash = self.__read_text_file(package.hash_file.file_path)
        calculated_hash = self.__calculate_hash(package.zip_file.file_path)
        print(f'Stored hash: {stored_hash}\nCalculated hash: {calculated_hash}')

        return stored_hash == calculated_hash

    def __read_text_file(self, file_path):
        with open(file_path, 'r') as file:
            file_content = file.read()
        return file_content

    def __calculate_hash(self, file_path):
        sha256 = hashlib.sha256()  # Create a new SHA-256 hash object

        with open(file_path, 'rb') as file:
            # Read the file in chunks and update the hash object
            while True:
                data = file.read(65536)
                if not data:
                    break
                sha256.update(data)

        return sha256.hexdigest()
