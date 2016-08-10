#!/usr/bin/env python3
"""Delete possibly unneeded files.

"""

import os

# Walk the tree
def walkTree(folder):
    """Walk tree and find unnecessarily large files.Walk
        Arg:
            folder: path that needs to be walked
    """
    folder = os.path.abspath(folder)
    for folder, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            # Newer better way to join strings
            filepath = ''.join( (folder,"/",filename) )
            # Return filestat
            filesize = os.path.getsize(filepath)
            # Print out the size of file from stat
            if filesize > 100000000:
                print(filepath)

if __name__ == "__main__":
    walkTree("/home/ubuntu/someDir")