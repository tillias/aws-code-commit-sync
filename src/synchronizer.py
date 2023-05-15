import hashlib

from settings import HASH_EXTENSION, PACKAGE_EXTENSION


class Synchronizer:
    def validate_package(self, package_name):
        stored_hash = self.read_text_file(package_name + HASH_EXTENSION)
        calculated_hash = self.calculate_hash(package_name + PACKAGE_EXTENSION)
        print(f'Stored hash: {stored_hash}\nCalculated hash: {calculated_hash}')

        return stored_hash == calculated_hash

    def read_text_file(self, file_path):
        with open(file_path, 'r') as file:
            file_content = file.read()
        return file_content

    def calculate_hash(self, file_path):
        sha256 = hashlib.sha256()  # Create a new SHA-256 hash object

        with open(file_path, 'rb') as file:
            # Read the file in chunks and update the hash object
            while True:
                data = file.read(65536)
                if not data:
                    break
                sha256.update(data)

        return sha256.hexdigest()
