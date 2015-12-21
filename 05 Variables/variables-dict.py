#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    # d= {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
    d = dict(
        one=1,
        two=2,
        three=3,
        four=4,
        five='five'
    )
    d['seven'] = 7
    for i in sorted(d.keys()):
        print(i, d[i])

if __name__ == "__main__": main()
