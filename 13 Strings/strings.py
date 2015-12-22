#!/usr/bin/python3
# strings.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    s = 'this  is a string'
    print('Capitalize', s.capitalize())
    print('Title', s.title())
    print('Upper', s.upper())
    print('Swapcase', s.swapcase())
    print("Find 'is'", s.find('is'))
    print("Replace 'this' with 'that'", s.replace('this', 'that'))
    print('Strip', s.strip())
    print('IsAlNum', s.isalnum())
    print('IsAlpha', s.isalpha())
    print('IsDigit', s.isdigit())
    print('IsPrintable', s.isprintable())


if __name__ == "__main__": main()
