#!/usr/bin/python3

# Selective Copy

# Searches for a certain file extension. Copy from whereever they are into a new
# folder.

import os
import shutil

# Find the extension by walking the tree
def findExt(folder,extension,destination):
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
    print("To copy:"+argpath)
    shutil.copy(argpath,argdest)
    

if __name__ == "__main__":
    myPath="/home/ubuntu/someDir"
    myExtension="jpg"
    myDest="/home/ubuntu"
    findExt(myPath,myExtension,myDest)