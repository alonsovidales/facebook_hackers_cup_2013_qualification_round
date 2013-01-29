#!/usr/bin/env python

import fileinput, re, itertools

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-01-26"

class BalancedSmiles:
    __string = None

    def __checkIfBalanced(self, inStr):
        bracketsOpened = 0
        for char in inStr:
            if char == '(':
                bracketsOpened += 1
            elif char == ')':
                bracketsOpened -= 1

            if bracketsOpened < 0:
                return False

        if bracketsOpened <> 0:
            return False

        return True

    def resolve(self):
        # Map all the possible smiles on the string
        smilesPositions = [pos.start() for pos in re.finditer(':\(', self.__string)] + [pos.start() for pos in re.finditer(':\)', self.__string)]

        if self.__checkIfBalanced(list(self.__string)):
            return "YES"

        for count in xrange(1, len(smilesPositions) + 1):
            for toRemove in itertools.combinations(smilesPositions, count):
                newStr = list(self.__string)
                for remove in toRemove:
                    newStr[remove] = '-'
                    newStr[remove + 1] = '-'

                if self.__checkIfBalanced(newStr):
                    return "YES"

        return "NO"


    def __init__(self, inString):
        self.__string = inString


if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]

    for linePos in xrange(1, int(lines[0]) + 1):
        print "Case #%s: %s" % (linePos, BalancedSmiles(lines[linePos]).resolve())
