import pathlib

def get_package_root():
    return pathlib.Path(__file__).parent.parent