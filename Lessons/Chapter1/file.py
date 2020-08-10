import os
from os import path
from datetime import date, time, timedelta
from datetime import datetime
import time
import shutil

def main():
    print(os.name)
    displayModificationTime()
    performShellCommands()


def readWriteFile():
        # Open a file in write mode
    f = open('test.txt', 'w+')

    # write content
    for i in range(10):
        f.write('Line ' + str(i) + '\n')

    # close the file handle
    f.close()

    # Open a file in append mode
    f = open('test.txt', 'a')

    for i in range(i, 20):
        f.write('Line ' + str(i) + '\n')

    # close the file handle
    f.close()   

    # Open a file in read mode
    f = open('test.txt', 'r')

    # read the content
    contents = f.read()             

    print(contents)

def performShellCommands():
    if path.exists("test.txt"):
        # get the source path of the file
        src = path.realpath("test.txt")
        dst = src + ".bak"
        shutil.copy(src, dst)
        # rename a file
        os.rename("test.txt", "test2.txt")


def displayModificationTime():
        # display the file path
    print("test.txt exists = " + str(path.exists("test.txt")))
    print("test.txt is a file = " + str(path.isfile("test.txt")))
    print("test.txt is a directory = " + str(path.isdir("test.txt")))
    print("test.txt resides in = " + str(path.realpath("test.txt")))
    print("test.txt resides in dir = " + str(path.split(path.realpath("test.txt"))))

    # display file modification time
    fmdt = path.getmtime("test.txt")
    mt = time.ctime(fmdt)
    print("test.txt was modified at = " + mt)
    td = datetime.now() - datetime.fromtimestamp(fmdt)
    print("It has been " + str(td) + " since test.txt was modified")
    print("It has been " + str(td.total_seconds()) + " seconds since test.txt was modified")    

if __name__ == "__main__":
    main()