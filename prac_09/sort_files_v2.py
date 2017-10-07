"""
CP1404 Practical
File moving based on user input exercise
"""
import shutil
import os


def main():
    """Move files with the os module."""
    # change to desired directory
    os.chdir('FilesToSort')
    extention_dict = {}
    for filename in os.listdir('.'):
        if not os.path.isdir(filename):
            file_ext = os.path.splitext(filename)[1].replace(".", "")
            #print(extention_dict[file_ext])
            if file_ext not in extention_dict:
                file_category = input("What category would you like to sort .{} files into?".format(file_ext))
                extention_dict[file_ext] = file_category
                make_ext_dir(file_category)
            shutil.copy(filename, './' + extention_dict[file_ext] + '/' + filename)
            #print(extention_dict[file_ext])
    print(extention_dict)
    #print("files successfully copied to subfolders")


def make_ext_dir(file_ext):
    """make a new directory if not already exists."""
    try:
        os.mkdir(file_ext)
    except (FileExistsError, FileNotFoundError):
        # do nothing
        pass

main()
