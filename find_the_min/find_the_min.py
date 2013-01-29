#!/usr/bin/env python

import fileinput

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-01-26"

class FindTheMin:
    __debug = False

    def __getMinNum(self, inArr):
        # Use an array of integers in order to determinate the cuttent numbers in use,
        # this array will use as key the number, and value, the number of times that
        # the integer is found
        if self.__arrayByPos == None:
            self.__arrayByPos = [0] * len(inArr)

            for value in inArr:
                if value < len(inArr):
                    self.__arrayByPos[value] += 1

        # Loop over all the integers in ascending order in order to find the firs integer
        # that is not contained in the array
        for count in xrange(0, len(inArr)):
            if self.__arrayByPos[count] == 0:
                self.__arrayByPos[count] += 1
                return count

        return len(inArr)

    def resolve(self):
        arrayToCheck = [self.__a]

        # Create the array with the first k positions using the given formula
        for pos in xrange(1, self.__k):
            arrayToCheck.append((self.__b * arrayToCheck[pos - 1] + self.__c) % self.__r)

        if self.__debug:
            print "Array: %s" % (arrayToCheck)
            print "Sorted: %s" % (sorted(arrayToCheck))

        # Check the number of remaining iterations to obtain the solution
        if (self.__k * 2) < self.__n:
            loopTo = self.__k
        else:
            loopTo = self.__n - self.__k

        # Move all the array pieces in order to obtain the smallest integers only
        for pos in xrange(0, loopTo):
            arrayToCheck.append(self.__getMinNum(arrayToCheck))
            lastNum = arrayToCheck.pop(0)

            if lastNum < len(self.__arrayByPos):
                self.__arrayByPos[lastNum] -= 1

        if self.__debug:
            print "Min ints Array: %s" % (sorted(arrayToCheck))

        # Now we have an array with the smallest integers possible, and who will repeate the same positions
        # on a croncreet number of loop. We will try to locate a number at the end of the array repeated on
        # a period of loops multiple of the remainig loops
        patterns = {}
        lastNum = self.__getMinNum(arrayToCheck)
        for count in xrange(self.__k * 2, self.__n):
            arrayToCheck.append(lastNum)
            lastNum = arrayToCheck.pop(0)

            # Cech if this number was previosly found on one of the iterations, if not, add it to the patters
            # list, or if it was, try to check if the necessary number of loops are a multiple of the remaining
            # loops in this case we know that the number will be at the end after finish all the loops
            if lastNum not in patterns:
                patterns[lastNum] = count
            else:
                distance = count - patterns[lastNum]
                if ((self.__n - count - 2) % distance) == 0:
                    return lastNum

                patterns[lastNum] = count

        return arrayToCheck.pop()


    def __init__(self, inN, inK, inA, inB, inC, inR):
        if self.__debug:
            print "---- N: %s K: %s A: %s B: %s C: %s R: %s ----" % (inN, inK, inA, inB, inC, inR)

        self.__arrayByPos = None
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
