from os import walk


def list_folder(src):
    (path, _, filenames) = next(walk(src))
    filenames.sort()
    return path, filenames


def get_json(file):
    f = open(file, "r")
    raw_array = f.readlines()
    raw = ''.join(map(str, raw_array))
    import json
    return json.loads(raw)

