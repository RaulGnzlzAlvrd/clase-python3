import os

def format_quotes(s):
    if '\'' in s:
        return '"%s"' % s
    else:
        return "'%s'" % s

def get_hash(file_path):
    cmd = "md5sum %s" % format_quotes(file_path)
    fp = os.popen(cmd)
    hash = fp.read().split()[0]
    fp.close()
    return hash

def has_extension(file_name, extension):
    return file_name.split(".")[-1] == extension

def search_duplicates(root="./", extension="mp3", files=dict()):
    path, dirnames, filenames = os.walk(root).__next__()
    path = os.path.abspath(path)
    for file in filenames:
        file_path = os.path.join(path, file)
        if has_extension(file_path, extension):
            files.setdefault(get_hash(file_path), []).append(file_path)
    for dir in dirnames:
        dir_path = os.path.join(path, dir)
        search_duplicates(dir_path, extension, files)
    return files

def print_duplicates(d):
    for hash, paths in d.items():
        if len(paths) > 1:
            print(paths)

d = search_duplicates("/home/raul-ga/Música")
print_duplicates(d)
