#!/usr/bin/env python

import fileinput

class BeautifulStrings:
    __string = None
    __allowedCahrs = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

    def resolve(self):
        string = self.__string.lower()
        chars = {}
        for char in list(string):
            if char in self.__allowedCahrs:
                if char in chars:
                    chars[char] += 1
                else:
                    chars[char] = 1

        totalValue = 0
        maxValue = 26
        for letters in sorted(chars.values(), reverse = True):
            totalValue += maxValue * letters
            maxValue -= 1

        return totalValue

    def __init__(self, inString):
        self.__string = inString


if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]

    for linePos in xrange(1, int(lines[0]) + 1):
        print "Case #%s: %s" % (linePos, BeautifulStrings(lines[linePos]).resolve())
