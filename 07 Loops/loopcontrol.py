#!/usr/bin/python3
# break.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    s = 'this is a string'
    for c in s:
        # if c == 's': continue # moves on
        # if c == 's': break # break out of the loop
        print(c, end='')
    else: # when the condition becomes false
        print('\nelse')

if __name__ == "__main__": main()
