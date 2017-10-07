"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import shutil
import os


def main():
    """Demo file renaming with the os module."""
    # change to desired directory
    os.chdir('Lyrics')
    print("Current directory is", os.getcwd())
    for dir_name, subdir_list, file_list in os.walk('.'):
        if len(file_list) != 0 and dir_name[-5:] != '\\temp':
            print("\nNow processing directory:\n\t", dir_name, "\nNew Files names are:")
            make_temp_dir(dir_name)
            for filename in file_list:
                new_name = get_fixed_filename(filename)
                print("\t", new_name)
                shutil.copy(dir_name + '/' + filename, dir_name + '/temp/' + new_name)
    print("\nAll files renamed and moved to temp folders within subfolder")


def make_temp_dir(dir_name):
    """make a new directory if not already exists."""
    try:
        os.mkdir(dir_name + '\\temp')
    except FileExistsError:
        # do nothing
        pass


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = ""
    # split the file name from the file extension and convert spaces to underscores
    file_name_segment = os.path.splitext(filename)[0].replace(' ', '_')
    # replace .TXT with .txt (or change to .lower if all file extensions to be lower case)
    file_ext = os.path.splitext(filename)[1].replace('.TXT', '.txt')
    # fix camel case (add underscore in front of each uppercase letter that isn't preceded by parenthesis or underscore)
    for x, letter in enumerate(file_name_segment):
        if x != 0 and letter.isupper() and file_name_segment[x-1] not in ('(', '_'):
            new_name += "_" + letter
        elif letter == '(' and file_name_segment[x-1] != '_':
            new_name += "_" + letter
        elif file_name_segment[x-1] == "'":  # needed for titles with "it's" in the string i.e. "It'syourblood"
            new_name = new_name.replace("'", "") + letter + "_"
        else:
            new_name += letter
    # now convert each word to title case and add file extention back in
    new_name_words = new_name.split('_')
    new_name = "{}{}".format("_".join("{}".format(word.title()) for word in new_name_words), file_ext)
    return new_name

main()
