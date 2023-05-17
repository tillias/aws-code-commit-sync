import subprocess


class GitHelper2:
    """Uses external git"""

    def __init__(self):
        pass

    def status(self, path):
        print(f'git -C {path} status')
        try:
            output = subprocess.check_output(['git', '-C', path, 'status'])
            print(output.decode())
            return output.decode()
        except subprocess.CalledProcessError as e:
            print('Error executing git status:', e)
            return None

    def chechout(self, path, branch):
        print(f'git -C {path} checkout {branch}')
        try:
            output = subprocess.check_output(['git', '-C', path, 'checkout', branch])
            return output.decode()
        except subprocess.CalledProcessError as e:
            print(f'Error executing git checkout {branch}', e)
            return None

    def commit(self, path, message):
        print(f'git -C {path} commit -m \'{message}\'')
        try:
            output = subprocess.check_output(['git', '-C', path, 'commit', '-m', f'\'{message}\''])
            return output.decode()
        except subprocess.CalledProcessError as e:
            print(f'Error executing git commit -m {message}', e)
            return None

    def add_all(self, path):
        print(f'git -C {path} add --all')
        try:
            output = subprocess.check_output(['git', '-C', path, 'add', '--all'])
            return output.decode()
        except subprocess.CalledProcessError as e:
            print('Error executing git add --all:', e)
            return None
