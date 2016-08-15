#!/usr/bin/env python3
"""Filling in the gaps.
File all files with a given prefix, then locate any gaps in numbering. Rename all later files to close the gap.

"""

import os
import re
from pprint import pprint
from pathlib import Path

def extract_filenames(argpath,argprefix):
    """Extract filenames and add the gap file.
        Args:
            argpath - Path where the sequence is located
            argprefix - The prefix of the existing files
    """
    regex = re.compile(str(argprefix)+r'(\d+).*')
    argpath = os.path.abspath(argpath)
    filenames = os.listdir(argpath)
    matches = [i for i in filenames if i.startswith(argprefix)]
    gap = find_gap(matches,argprefix,regex)
    p = Path("{}/{}{}".format(argpath, argprefix, gap)).touch()


def find_gap(arglist,argprefix,argregex):
    """Find the single gap in the list of ints.
        Args:
            arglist - list with the gap in it
            argprefix - prefix to be checked against
            argregex - Regex object to check against
        Returns:
            Missing int in the sequence
    """
    matches = [int(argregex.match(i).group(1)) for i in arglist]
    matches.sort()
    the_sum = sum(matches)
    total = (max(matches)+1)*max(matches)/2
    return int(total - the_sum)


def main():
    """Run the program.
    """
    extract_filenames("/tmp/testpath","stub")

if __name__ == "__main__":
    main()