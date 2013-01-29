#!/usr/bin/env python

import fileinput, re, itertools

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-01-26"

class FindTheMin:
    __debug = False

    def __getMinNum(self, inArr):
        sortedArray = sorted(list(set(inArr)))
        for pos in xrange(0, len(inArr)):
            if pos <> sortedArray[pos]:
                return pos

        return pos + 1

    def __checkIfMinNumbers(self, inArray):
        if inArray[0] == 0:
            for pos in xrange(0, len(inArray)):
                if pos <> inArray[pos]:
                    return False

            return True

        return False

    def resolve(self):
        arrayToCheck = [self.__a]

        for pos in xrange(1, self.__k):
            arrayToCheck.append((self.__b * arrayToCheck[pos - 1] + self.__c) % self.__r)

        if self.__debug:
            print "Array: %s" % (arrayToCheck)
            print "Sorted: %s" % (sorted(arrayToCheck))

        patternFound = False
        for count in xrange(self.__k, self.__n):
            arrayToCheck.append(self.__getMinNum(arrayToCheck))
            arrayToCheck.pop(0)

            if False:
                if self.__checkIfMinNumbers(arrayToCheck):
                    jumpToPos = ((int((self.__n - count) / (self.__k + 1)) * (self.__k + 1)) + count)
                    print "JUMPING!!!!"
                    if self.__debug:
                        print "New Pos: %s" % (jumpToPos)
                    for countMin in xrange(jumpToPos + 1, self.__n):
                        arrayToCheck.append(self.__getMinNum(arrayToCheck))
                        arrayToCheck.pop(0)

                    return arrayToCheck.pop()

        return arrayToCheck.pop()


    def __init__(self, inN, inK, inA, inB, inC, inR):
        if self.__debug:
            print "---- N: %s K: %s A: %s B: %s C: %s R: %s ----" % (inN, inK, inA, inB, inC, inR)

        self.__n = inN
        self.__k = inK
        self.__a = inA
        self.__b = inB
        self.__c = inC
        self.__r = inR


if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]

    for case in xrange(0, int(lines[0])):
        [n, k] = map(int, lines[(case * 2) + 1].split())
        [a, b, c, r] = map(int, lines[(case * 2) + 2].split())
        print "Case #%s: %s" % (case + 1, FindTheMin(n, k, a, b, c, r).resolve())
