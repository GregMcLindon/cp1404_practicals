"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import shutil
import os

def main():
    """Demo file renaming with the os module."""
    #print("Current directory is", os.getcwd())

    # change to desired directory
    os.chdir('Lyrics/Christmas')
    # print a list of all files (test)
    #print(os.listdir('.'))
    make_temp_dir()

    # loop through each file in the (original) directory
    for filename in os.listdir('.'):
        # ignore directories, just process files
        if not os.path.isdir(filename):
            new_name = get_fixed_filename(filename)
            #print(new_name)

            # Option 1: rename file to new name - in place
            #os.rename(filename, new_name)

            # Option 2: move file to new place, with new name
            shutil.copy(filename, 'temp/' + new_name)
    os.chdir('temp')
    print("Files renamed and moved to:\n{}".format(os.getcwd()))

            # Processing subdirectories using os.walk()

            # os.chdir('..')  # .. means "up" one directory
            # for dir_name, subdir_list, file_list in os.walk('.'):
            #     print("In", dir_name)
            #     print("\tcontains subdirectories:", subdir_list)
            #     print("\tand files:", file_list)

def make_temp_dir():
    """make a new directory if not already exists."""
    try:
        os.mkdir('temp')
    except FileExistsError:
        # do nothing
        print("exists")

def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = ""
    # split the file name from the file extension
    file_name_segment = os.path.splitext(filename)[0].replace(' ', '_')
    # replace .TXT with .txt (or change to .lower if all files to be lower case)
    file_ext = os.path.splitext(filename)[1].replace('.TXT', '.txt')
    # fix camel case (add underscore in front of each uppercase letter that isn't preceded by parenthesis or underscore)
    for x, letter in enumerate(file_name_segment):
        if x != 0 and letter.isupper() and file_name_segment[x-1] not in ('(', '_'):
            new_name += "_" + letter
        else:
            new_name += letter
    # now convert each word to title case and add file extention back in
    new_name_words = new_name.split('_')
    new_name = "{}{}".format("_".join("{}".format(word.title()) for word in new_name_words), file_ext)
    return new_name

main()
