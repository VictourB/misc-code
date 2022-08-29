#! python3
# backuptoZip.py - This program will create a backup of a folder and store it as a zip file on the users computer.

import zipfile, os

def prompt():
    print("\nThis program will backup a given directory into a compressed .zip file.")
    response = input("Please enter a directory to backup or press enter to quit. \n")
    if not response:
        return response
    if os.path.isdir(response):
        return response
    else:
        print("That is not a valid directory")
        return prompt()

def backuptoZip(folder):
    # Backup the entire contents of the folder into a zip file
    folder = os.path.abspath(folder) # Make sure the folder is absolute

    # Figure out the name of the filename based on what files already exists
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        number += 1

    # Create Zip File
    print('Creating %s...' % (zipFileName))
    with zipfile.ZipFile(zipFileName, 'w') as backupZip:

        # Walk the entire folder and compress files inside. print done
        for foldername, subfolders, filenames in os.walk(folder):

            print('Adding files in %s...' % (foldername))
            # Add the current folder to the ZIP file.
            backupZip.write(foldername)

            for filename in filenames:
                newBase = os.path.basename(folder) + '_'
                if filename.startswith(newBase) and filename.endswith('.zip'):
                    continue # don't backup the backup ZIP files

                backupZip.write(os.path.join(foldername, filename))

        print("Done!")

def main():
    folder = prompt()
    if not folder:
        return
    else:
        backuptoZip(folder)

    return main()

main()