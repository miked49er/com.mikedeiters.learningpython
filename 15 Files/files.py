#!/usr/bin/python3
# files.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    # buffersize = 100000 # byte size
    # infile = open('bigfile.txt', 'r')
    # outfile = open('new.txt', 'w')
    # buffer = infile.read(buffersize)
    # while len(buffer):
    #     outfile.write(buffer)
    #     print('.', end='')
    #     buffer = infile.read(buffersize)
    # print()
    # print('Done')
    read = 'olives.jpg'
    out = 'newpic.jpg'
    buffersize = 50000
    read_binary(read,out,buffersize)

def read_binary(read, out, buffersize):
    infile = open(read, 'rb')
    outfile = open(out, 'wb')
    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print('.', end='')
        buffer = infile.read(buffersize)
    print('\nDone.')

if __name__ == "__main__": main()
