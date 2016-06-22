#!/usr/bin/python3
# backupToZip.py - Copies an entire folder and its contents into a ZIP files
# whose filename increments.

import zipfile, os

def backupToZip(folder):
    # Backup the entire contents of "folder" into a ZIP file.

    folder = os.path.abspath(folder)

    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # create the ZIP files
    print('Creating %s...' % (zipFilename))
    backupToZip = zipfile.ZipFile(zipFilename, 'w')

    # TODO: walk the entire folder tree and compress the files into each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # Add the current folder to the ZIP file.
        backupToZip.write(foldername)
        # Add all files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupToZip.write(os.path.join(foldername, filename))
    backupToZip.close()
    print('Done.')

backupToZip('/home/ecmartz/someDir')
