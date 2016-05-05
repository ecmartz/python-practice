#!/usr/bin/env python3

import os
import sys
import re
from pprint import pprint


if __name__ == '__main__':
    path_to_open=os.getcwd()
    txtRegex = re.compile(r'.*\.txt')

    contents = os.listdir(path_to_open)
    myin = str(sys.argv[1])
    theRegex = re.compile(myin)
    
    for i in contents:
        if txtRegex.match(i):
            with open(i,'r') as fandle:
                line = fandle.read()
                if theRegex.search(line):
                    print("Found match in {}: {}".format(i, theRegex.search(line).group(0)))