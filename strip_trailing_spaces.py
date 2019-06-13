#!/usr/bin/env python

import sys

paths = sys.stdin.read().strip().split()
for p in paths:
    with open(p) as f:
        lines = f.read().split('\n')
    with open(p, 'w') as f:
        for l in lines:
            f.write(l.rstrip() + '\n')

