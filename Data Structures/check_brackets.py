# python3

from collections import namedtuple


# python3

import sys


class Bracket:


    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def match(self, char):


        if self.bracket_type == '[' and char == ']':
            return True
        if self.bracket_type == '{' and char == '}':
            return True
        if self.bracket_type == '(' and char == ')':
            return True
        return False


def checker(text):
    stack = []
    for index, char in enumerate(text, start=1):

        if char in ("[", "(", "{"):
            stack.append(Bracket(char, index))
        elif char in ("]", ")", "}"):
            if not stack:
                return index
            top = stack.pop()
            if not top.match(char):
                return index
    if stack:
        top = stack.pop()
        return top.position

    return "Success"


def main():
    text = map(str, input())
    mismatch = checker(text)
    # Printing answer, write your code here
    print(mismatch)
if __name__ == "__main__":
    main()







