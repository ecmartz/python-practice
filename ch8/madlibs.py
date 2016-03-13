#!/usr/bin/env python3

from sys import argv
import re

def usage():
    print('madlibs.py <input_file>')

if __name__ == '__main__':
    try:
        infile = argv[1]
    except IndexError:
        usage()
    else:
        print('Reading file: '+argv[1])
        
        outfile = infile+'-out.txt'
        
        #inhandle = open(infile,'r')
        outhandle = open(outfile,'w')
        
        # come up with regex to match ADJECTIVE, NOUN, ADVERB, and VERB
        reg = re.compile(r'NOUN|VERB|ADJECTIVE|ADVERB')
        # initialize array of matches
        matches = []
        
        # open input file and find all matches
        with open(infile, 'r') as inhandle:
            line = inhandle.read()
            matches.extend(reg.findall(line))
        
        # Open file again to begin replacements
        with open(infile, 'r') as inhandle:
            line = inhandle.read()
            # go through matches and prompt user for Mad Libs input
            for m in matches:
                if(m=='NOUN'):
                    print("Enter a noun:")
                if(m=='VERB'):
                    print("Enter a verb:")
                if(m=='ADJECTIVE'):
                    print("Enter a adjective:")
                if(m=='ADVERB'):
                    print("Enter a adverb:")
                
                stdin = input()
                
                # perform substitution of each user input
                line = re.sub(m,stdin,line,count=1)
        
        # write the output file
        with open(outfile,'w') as outhandle:
            outhandle.write(line)
        
        inhandle.close()
        outhandle.close()