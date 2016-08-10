#!/usr/bin/env python3
"""Selective Copy.
    Searches for a certain file extension. Copy from whereever they are into a new
    folder.
"""
import os
import shutil

# Find the extension by walking the tree
def findExt(folder,extension,destination):
    """Walk tree and find extension, then copy to destination.
        Args:
            folder: path to walk
            extension: extension to look for
            destination: path to copy matched file to
    """
    # Stuff
    folder = os.path.abspath(folder)
    
    for folder, subfolders, filenames in os.walk(folder):
        # Assuming Unix style
        for filename in filenames:
            filepath = str(folder)+'/'+str(filename)
            # Check filename for extension we care about
            if filepath.endswith("."+extension):
                doTheCopy(filepath,destination)

# Perform the copy to the new location
def doTheCopy(argpath,argdest):
    """Perform the actual copy.
        Args:
            argpath: path source
            argdest: path dest
    """
    print("To copy:"+argpath)
    shutil.copy(argpath,argdest)
    

if __name__ == "__main__":
    myPath="/home/ubuntu/someDir"
    myExtension="jpg"
    myDest="/home/ubuntu"
    findExt(myPath,myExtension,myDest)