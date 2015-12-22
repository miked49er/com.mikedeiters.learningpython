#!/usr/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print(testfunc(42))
    # testFunc2(42, 69, 101, 32, 21, 90)
    # testFunc3(one=1, two=2, four=42)

def testfunc(num, another = None): # None is a default value that is basically null
    return 'This is a test function'
    # pass # for place holder functions

def testFunc2(this, that, other, *args):
    print(this, that, other)
    for i in args: print(i, end='\n')

def testFunc3(**kwargs):
    # print(kwargs['one'], kwargs['two'], kwargs['four'])
    for i in kwargs:
        print(i, kwargs[i])

if __name__ == "__main__": main()
