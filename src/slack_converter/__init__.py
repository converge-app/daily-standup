from os import walk


def list_folder(src):
    (dirpath, _, filenames) = next(walk(src))
    return (dirpath, filenames)
