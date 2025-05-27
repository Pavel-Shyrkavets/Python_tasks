import os

class Cd:
    def __init__(self, path):
        if not (os.path.exists(path) and os.path.isdir(path)):
            raise ValueError
        self.path = path

    def __enter__(self):
        self.directory_name = os.getcwd()
        os.chdir(self.path)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        os.chdir(self.directory_name)
