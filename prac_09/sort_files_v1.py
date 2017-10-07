"""
CP1404 Practical
File moving based on file extention exercise
"""
import shutil
import os


def main():
    """Move files with the os module."""
    # change to desired directory
    os.chdir('FilesToSort')
    extention_list = []
    for filename in os.listdir('.'):
        if not os.path.isdir(filename):
            file_ext = os.path.splitext(filename)[1].replace(".", "")
            if file_ext not in extention_list:
                extention_list.append(file_ext)
                make_ext_dir(file_ext)
            shutil.copy(filename, './' + file_ext + '/' + filename)
    print("files successfully copied to subfolders")


def make_ext_dir(file_ext):
    """make a new directory if not already exists."""
    try:
        os.mkdir(file_ext)
    except (FileExistsError, FileNotFoundError):
        # do nothing
        pass

main()
