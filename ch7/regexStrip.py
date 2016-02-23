#!/usr/bin/env python3

import re

# arg1=string to match against, arg2=optional str to strip()
def regStrip(arg1, *arg2):
    if(arg2):
        arg = arg2[0]                                                                   # Get string from tuple
        print('Remove: '+str(arg))  
        check = r'^'+str(arg)+r'*([^'+str(arg)+r']?.*[^'+str(arg)+r'])'+str(arg)+r'*$'  # Build raw string
        aRemove = re.compile(check)
        groups = aRemove.findall(arg1)
        for i, v in enumerate(groups):
            print("'"+v+"'")                                                            # Print in an easy format
    else:
        print('Just remove whitespace')                                                 # could be one function
        wsRemove = re.compile(r'^\s*([^\s]?.*[^\s])\s*$')                               # Default (space)
        groups = wsRemove.findall(arg1)
        for i, v in enumerate(groups):
            print("'"+v+"'")

if __name__ == '__main__':
    regStrip('  a b  c   e     ghij  k      ')                                          # Try with default
    regStrip('____abc__123_d__s___','_')                                                # Try with custom