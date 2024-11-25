import os
import tarfile

from . import env

def pack(output_path, src_path=None):
    src_path = src_path or env.get()

    with tarfile.open(output_path, "w:gz") as tar:
        tar.add(src_path, arcname=os.path.basename(src_path))


def unpack(tar_path, dest_path=None):
    
    dest_path = dest_path or env.get()

    with tarfile.open(tar_path, "r:gz") as tar:
        tar.extractall(path=dest_path)
