"""
CP1404 Practical
Check files for copywrite content
"""
import os
from operator import itemgetter
COPYWRITE_STRING = ".i ©"


def main():
    """Check files to see if they contain copywrite information."""
    # change to desired directory
    os.chdir('Lyrics')
    copywrite_missing_dict = {}
    for dir_name, subdir_list, file_list in os.walk('.'):
        if len(file_list) != 0:
            for filename in file_list:
                song_file = open(os.path.join(dir_name, filename), 'r')
                file_text = song_file.read()
                song_file.close()
                if COPYWRITE_STRING not in file_text:
                    copywrite_missing_dict[filename] = os.path.join(dir_name, filename)
    print("The following songs are missing copy-write information:")
    print("\n".join("{:40}{:60}".format(song_title, os.path.dirname(song_location)) for song_title,
                song_location in sorted(copywrite_missing_dict.items(), key=itemgetter(1, 0))))

main()
