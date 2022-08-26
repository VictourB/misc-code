#! python3
# By Victour Bue

# Large File Finer
# It’s not uncommon for a few unneeded but humongous files or folders to take up the
# bulk of the space on your hard drive. If you’re trying to free up room on your
# computer, you’ll get the most bang for your buck by deleting the most massive of
# the unwanted files. But first you have to find them.
# Write a program that walks through a folder tree and searches for exceptionally
# large files or folders—say, ones that have a file size of more than 100MB.
# (Remember, to get a file’s size, you can use os.path.getsize() from the os
# module.) Print these files with their absolute path to the screen.

import os, math

def prompt():
    print("""
    
    Large File Finder
    This program searches an inputed directory and prints all files large then the user specified size.

    """)
    response = input("Would you like to do that? ")
    if response.lower() == "yes" or response.lower() == "no":
        return response.lower()
    else: 
        print("Please enter yes or no")
        return prompt()

def getDirectory():
    print("")
    print("Which directory tree would you like to search?")
    response = input()
    if not os.path.exists(response):
        print("That directory doesn't exist? Please try again.")
        return getDirectory()
    else:
        return response

def getSize():
    print("")
    print("What size of large files should I look for? Enter a number of kilobytes.")
    response = input()
    if not response.isdigit():
        print("That doesn't look like a number")
        return getSize()
    else:
        return int(response)

def displayLargeFiles(folder, size):
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            filePath = os.path.join(foldername, filename)
            fileSize = os.path.getsize(filePath)
            fileSizeStr = convertSize(fileSize)
            sizeStr = convertSize(size*1024)

            if  fileSize >= (size*1024):
                print(f"""
        Large file found at:                                
        {os.path.join(foldername, filename)}                
        Size: {fileSizeStr}
                """)

def convertSize(bytes):
    if bytes == 0:
        return "0B"
    sizeName = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(bytes, 1024)))
    p = math.pow(1024, i)
    s = round(bytes / p, 2)
    return "%s %s" % (s, sizeName[i])

def main():
    if prompt() == "no":
        print("exiting...")
        return

    directorytoSearch = getDirectory()
    sizetoSearch = getSize()
    displayLargeFiles(directorytoSearch, sizetoSearch)

    main()


main()
