import os
def get_data(path):
    
    root_files = {}
    root_dirs = {}
    for root, dirs, files in os.walk(path):#r"E:\Python 2.7.9\Scripts\2020\Dir Buster OS.WALK\XD"):
        root_files[root] = files
        root_dirs[root] = dirs
    return root_dirs, root_files

x = get_data(r'E:\Python 2.7.9\Scripts\2020\Dir Buster OS.WALK\XD')