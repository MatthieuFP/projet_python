import os

def get_relative_path():
    list_directories = os.path.dirname(__file__).split("\\")
    directories = list()
    for d in list_directories:
        directories.append(d)
        if d == 'src':
            break
    relative_path_src = "\\".join(directories)
    return relative_path_src
