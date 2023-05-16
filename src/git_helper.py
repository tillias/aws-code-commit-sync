import os
import shutil
import zipfile
from settings import EXTRACT_PATH
from secrets import GIT_USER_NAME, GIT_PASSWORD, GIT_REPO_URL
from dulwich.porcelain import clone, status, branch_create, add


class GitHelper:
    def __init__(self):
        pass

    def clone_repo(self, package_name):
        local_path = os.path.join(EXTRACT_PATH, package_name)

        if os.path.exists(local_path):
            print(f'Local path for git repo {local_path} exists. Cleaning up')
            shutil.rmtree(local_path)

        print('Cloning repo')
        clone(GIT_REPO_URL, local_path, checkout=True, username=GIT_USER_NAME, password=GIT_PASSWORD)

    def add_package_to_repo(self, package, branch_name):
        # TODO create branch and switch
        local_path = os.path.join(EXTRACT_PATH, package.package_name)
        branch_create(local_path, branch_name, force=True)

        self.__extract_package(package, local_path)

        print(f'Adding package from {local_path} to repo')
        add(local_path, local_path)
        rst = status(local_path)
        print(rst)
        # add(local_path, paths=local_path)
        #commit(repo, 'A sample commit')
        # push(local_path, GIT_REPO_URL, username=GIT_USER_NAME, password=GIT_PASSWORD)
        pass

    def __extract_package(self, package, local_path):
        zip_path = package.zip_file.file_path

        print(f'Extracting package {zip_path} into {local_path}')

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(local_path)
