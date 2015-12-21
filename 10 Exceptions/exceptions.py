#!/usr/bin/python3
# exceptions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

def main():
    try:
        for line in readFile('xlines.doc'): print(line.strip())
    except IOError as e:
        print('Could not open file:', e)
    except ValueError as e:
        print(e)

def readFile(file):
    if (file.endswith('.txt')):
        fh = open(file)
        return fh.readlines()
    else:
        raise ValueError('file must end with .txt')

if __name__ == "__main__": main()
