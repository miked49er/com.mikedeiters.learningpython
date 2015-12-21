#!/usr/bin/python3
# for.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    # fh = open('lines.txt')
    # for index, line in enumerate(fh.readlines()):
    #     print(index, line, end='')
    str = 'This is a string'
    for i, char in enumerate(str):
        if char == 's': print('index {} is a s'.format(i))

if __name__ == "__main__": main()
