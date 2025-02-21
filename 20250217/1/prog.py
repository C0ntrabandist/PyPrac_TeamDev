import sys
import os
import zlib
import glob

if len(sys.argv) == 1:
    print("There are too few arguments.")
    exit(0)

path = sys.argv[1] + '/.git/refs/heads'


if len(sys.argv) == 2:
    for item in glob.iglob(path):
        direc = os.scandir(item)
        for branch in direc:
            print(branch.name)
	pass

else:
	pass
