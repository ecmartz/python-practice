#!/usr/bin/env python3

import re
from sys import argv

def checkPassword(arg):
    # Check for 8 chars
    try:
        if(len(str(arg))>=8):
            # Validate regex one lower, one upper, one number
            lowerChk = re.compile(r'[a-z]')
            upperChk = re.compile(r'[A-Z]')
            numChk   = re.compile(r'[0-9]')
            if( lowerChk.search(arg) != None and
                upperChk.search(arg) != None and
                numChk.search(arg)   != None):
                    print('Password is strong')
            else:
                print('Password needs 1 lower, 1 upper, and 1 number')
        else:
            print('Not enough characters')
    except(TypeError):
        print('Must be string.')
        raise

if __name__ == '__main__':
    checkPassword(argv[1])