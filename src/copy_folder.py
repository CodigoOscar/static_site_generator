import os
import shutil


def copy_folder(src, dest):
    if os.path.exists(dest):
        print(f"Deleting directory: {dest}")
        shutil.rmtree(dest)
    os.mkdir(dest)
    copy_contents(src, dest)


def copy_contents(src, dest):
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        if os.path.isfile(src_path):
            print(f"Copying file: {src_path} -> {dest_path}")
            shutil.copy(src_path, dest_path)
        else:
            print(f"Creating directory: {dest_path}")
            os.mkdir(dest_path)
            copy_contents(src_path, dest_path)
