# program that reads a file and takes
# Author : Dave Byrne :)

FILENAME = "numbers.txt"
DATADIR = "my_work/data/"
FULLPATH = DATADIR + FILENAME

print (FULLPATH)

with open(FULLPATH, "rt") as fp:
    for line in fp:
        print (line)