# IPython log file

import sys
import os

maxlength = int(sys.argv[1], base=0)

paths = sys.stdin.read().strip().split()
for p in paths:
    if not os.path.isfile(p):
        # print("{} is not a file".format(p))
        continue

    with open(p, 'r') as f:
        for i, l in enumerate(f):
            if len(l) > maxlength:
                print("{}: Line #{} is too long! Expected 80 chars, found {}".format(p, i, len(l)))


