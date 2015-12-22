#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Animal:
    def talk(self):print('I have something to say')
    def walk(self):print("Hey I'm walking here")
    def clothes(self):print('I have nice close')

class Duck(Animal):
    def __init__(self, **kwargs):
        self._variables = kwargs

    def quack(self):
        print('Quaaack!')

    def walk(self):
        # super().walk()
        print('Walks like a duck.')

    def bark(self):print('A Duck cannot bark')

    def fur(self):print('A Duck has feathers')

    # def get_color(self):
    #     return self.variables.get('color', None)
    #
    # def set_color(self, color):
    #     self.variables['color'] = color

    def set_variable(self, key, value):
        self._variables[key] = value

    def get_variable(self, key):
        return self._variables.get(key)

class Dog(Animal):
    def fur(self):print('I have brown and white fur')

    def bark(self):print('Woof!')

    def walk(self):print('Walks like a dog')

    def quack(self):print('A dog cannot quack')

def in_the_forest(dog):
    dog.bark()
    dog.fur()

def in_the_pond(duck):
    duck.quack()
    duck.walk()

def main():
    donald = Duck()
    donald.set_variable('feet', 2)
    donald.set_variable('color', 'blue')
    # print('Color', donald.get_variable('color'))
    # print('# of Feet', donald.get_variable('feet'))
    fido = Dog()

    for o in (donald, fido):
        in_the_forest(o)
        in_the_pond(o)

if __name__ == "__main__": main()
