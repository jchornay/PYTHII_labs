# Jonathan Chornay
# CMSY 257 Spring 2023 Class
# Professor Charles Edwards
#
# Lab 3 Problem 1

import os


def main():
    repeat = True

    while repeat:

        # gets file path from user
        path = input("Enter directory name: ").strip()
        # try block that passes file path to getFileCount method
        try:
            print(f"The number of files and folders in {path} is {str(getFileCount(path))}")
            success = True
        except:
            success = False
            print("Directory does not exist")

        # if try block is successful, offers user option to view file names
        if success:
            if input("\nView file names? Y/N ").lower().strip() == "y":
                getFileNames(path)

        # offers user option to search a new directory
        if input("\nSearch another directory? Y/N ").lower().strip() != "y":
            repeat = False


def getFileCount(path):
    # takes user input and passes to os.listdir method, returning length of list
    return os.listdir(path).__len__()


def getFileNames(path):
    print("File or folder names:\n")

    # takes user input and passes to os.listdir method, returning contents of list
    for i in os.listdir(path): print(i)


if __name__ == '__main__':
    main()
