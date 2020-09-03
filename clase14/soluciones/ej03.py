import os

def get_hash(file_path):
    cmd = "md5sum '%s'" % file_path
    fp = os.popen(cmd)
    hash = fp.read()[0]
    fp.close()
    return hash

def has_extension(file_name, extension):
    return file_name.split(".")[-1] == extension

def search_duplicates(root="./", extension="mp3", files=dict(), duplicates=dict()):
    path, dirnames, filenames = os.walk(root).__next__()
    path = os.path.abspath(path)
    for file in filenames:
        file_path = os.path.join(path, file)
        if has_extension(file_path, extension):
            hash = get_hash(file_path)
            paths = d.setdefault(hash, [])
            paths.append(file_path)
            if len(paths) > 1:
                duplicates[hash] = paths
    for dir in dirnames:
        dir_path = os.path.join(path, dir)
        search_duplicates(dir_path, extension, files, duplicates)
    return duplicates

search_duplicates("/home/raul-ga/Música")
