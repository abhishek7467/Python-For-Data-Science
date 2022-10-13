'''An Application which returns the size in bytes, KB or MB '''


import os
def convert(num):
    for x in ['bytes','KB','MB','GB']:
        if num<1024.0:
            return(num, x)
        num/=1024

def file_size(file_path):
    if os.path.isfile(file_path):
        file_info=os.stat(file_path)
    return convert(file_info.st_size)

